#encoding: utf-8
from __future__ import print_function
from builtins import str
import ipaddress
import datetime
import os
import sys
from twisted.names import client, dns, server, hosts as hosts_module, root, cache, resolve
from twisted.internet import reactor
from twisted.python.runtime import platform

TTL = 0
dict = {}
dont_print_ip_ranges = ['172.253.0.0/16','172.217.0.0/16']
dont_rebind_nameservers = ["ns1.", "ns2."]
FILENAME = "dns-log-" + str(datetime.datetime.now().strftime("%H-%M-%S.%f-%d-%m-%Y"))+'.log'
WHITELISTEDIP = ''
INTERNALIP = ''
SERVERIP = ''
PORT = 53
DOMAIN = ''


def OpenLogFile():
    global f
    major = sys.version_info[0]
    if major == 3:
        f = open(FILENAME, 'a')
    else:
        f = open(FILENAME, 'ab')


def CloseLogFile():
    f.close()


def search_file_for_all(hosts_file, name):
    results = []
    if name.decode().lower() not in dont_rebind_nameservers:
        if name not in dict or dict[name] < 1:
            ip = WHITELISTEDIP
        else:
            ip = INTERNALIP
        if name not in dict:
            dict[name] = 0
        dict[name] += 1
    else:
        ip = SERVERIP
    print('================================================================================================')
    print("ServerTime - A record: ",datetime.datetime.now().strftime("%H:%M:%S.%f %d-%m-%Y"), sep='')
    print('Response with A record: ', name.decode('utf-8'), ' -> ', ip, sep='')
    print('================================================================================================')
    OpenLogFile()
    print('================================================================================================', file=f)
    print("ServerTime - A record: ",datetime.datetime.now().strftime("%H:%M:%S.%f %d-%m-%Y"), sep='', file=f)
    print('Response with A record: ', name.decode('utf-8'), ' -> ', ip, sep='', file=f)
    print('================================================================================================', file=f)
    CloseLogFile()
    results.append(hosts_module.nativeString(ip))
    return results


class Resolver(hosts_module.Resolver):
    def _aRecords(self, name):
        return tuple([
            dns.RRHeader(name, dns.A, dns.IN, TTL, dns.Record_A(addr, TTL))
            for addr in search_file_for_all(hosts_module.FilePath(self.file), name)
            if hosts_module.isIPAddress(addr)
        ])


class PrintClientAddressDNSServerFactory(server.DNSServerFactory):
    def check_network(self, network):
        for dont_print_ip_range in dont_print_ip_ranges:
            if ipaddress.ip_address(u"%s" % network) in ipaddress.ip_network(u"%s" % dont_print_ip_range):
                return True
        return False


    def buildProtocol(self, addr):
        if not self.check_network(addr.host):
            print('------------------------------------------------------------------------------------------------')
            print("ServerTime - DNSServerFactory: ",datetime.datetime.now().strftime("%H:%M:%S.%f %d-%m-%Y"), sep='')
            print("Request: Connection to DNSServerFactory from: ", addr.host," on port: ",addr.port," using ",addr.type,sep='')
            print('------------------------------------------------------------------------------------------------')
            OpenLogFile()
            print('------------------------------------------------------------------------------------------------', file=f)
            print("ServerTime: - DNSServerFactory: ",datetime.datetime.now().strftime("%H:%M:%S.%f %d-%m-%Y"), file=f, sep='')
            print("Request: Connection to DNSServerFactory from: ", addr.host," on port: ",addr.port," using ",addr.type, file=f, sep='')
            print('------------------------------------------------------------------------------------------------', file=f)
            CloseLogFile()
        return server.DNSServerFactory.buildProtocol(self, addr)


class PrintClientAddressDNSDatagramProtocol(dns.DNSDatagramProtocol):
    def check_network(self, network):
        for dont_print_ip_range in dont_print_ip_ranges:
            if ipaddress.ip_address(u"%s" % network) in ipaddress.ip_network(u"%s" % dont_print_ip_range):
                return True
        return False


    def datagramReceived(self, datagram, addr):
        if not self.check_network(addr[0]):
            print('------------------------------------------------------------------------------------------------')
            print("ServerTime - DNSDatagramProtocol: ",datetime.datetime.now().strftime("%H:%M:%S.%f %d-%m-%Y"), sep='')
            print("Request: Datagram to DNSDatagramProtocol from: ", addr[0], " on port: ", addr[1], sep='')
            print('------------------------------------------------------------------------------------------------')
            OpenLogFile()
            print('------------------------------------------------------------------------------------------------', file=f)
            print("ServerTime - DNSDatagramProtocol: ",datetime.datetime.now().strftime("%H:%M:%S.%f %d-%m-%Y"), file=f, sep='')
            print("Request: Datagram to DNSDatagramProtocol from: ", addr[0], " on port: ", addr[1], file=f, sep='')
            print('------------------------------------------------------------------------------------------------', file=f)
            CloseLogFile()
        return dns.DNSDatagramProtocol.datagramReceived(self, datagram, addr)


def create_resolver(servers=None, resolvconf=None, hosts=None):
    if platform.getType() == 'posix':
        if resolvconf is None:
            resolvconf = b'/etc/resolv.conf'
        if hosts is None:
            hosts = b'/etc/hosts'
        the_resolver = client.Resolver(resolvconf, servers)
        host_resolver = Resolver(hosts)
    else:
        if hosts is None:
            hosts = r'c:\windows\hosts'
        from twisted.internet import reactor
        bootstrap = client._ThreadedResolverImpl(reactor)
        host_resolver = Resolver(hosts)
        the_resolver = root.bootstrap(bootstrap, resolverFactory=client.Resolver)
    return resolve.ResolverChain([host_resolver, cache.CacheResolver(), the_resolver])


def main(port):
    factory = PrintClientAddressDNSServerFactory(
        clients=[create_resolver(servers=[('8.8.8.8', 53)], hosts='hosts')],
    )
    protocol = PrintClientAddressDNSDatagramProtocol(controller=factory)
    reactor.listenUDP(PORT, protocol)
    reactor.listenTCP(PORT, factory)
    print('-------------------------------------------------------------------------------------------------------------')
    print("DNS Server started...\nListening on 0.0.0.0:" + str(PORT))
    print("Log file name: " + FILENAME)
    print("Not showing/logging requests from IP range: " + ', '.join(dont_print_ip_ranges))
    print("Not rebinding requests for A records: " + ', '.join(dont_rebind_nameservers) + " -> " + SERVERIP)
    print('-------------------------------------------------------------------------------------------------------------\n\n')
    reactor.run()


if __name__ == '__main__':
    if len(sys.argv) != 6:
        print("Usage: python "+sys.argv[0]+" WhitelistedIP InternalIP ServerIP Port Domain")
        print ("Example: python "+sys.argv[0]+" 216.58.214.206 169.254.169.254 78.47.24.216 53 localdomains.pw")
        exit(1)
    else:
        WHITELISTEDIP = sys.argv[1]
        INTERNALIP = sys.argv[2]
        SERVERIP = sys.argv[3]
        PORT = int(sys.argv[4])
        DOMAIN = sys.argv[5]
        dont_rebind_nameservers = [dont_rebind_nameservers[0] + DOMAIN, dont_rebind_nameservers[1] + DOMAIN]
    main(PORT)
