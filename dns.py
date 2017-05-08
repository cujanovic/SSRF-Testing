 #encoding: utf-8
import re
import os
import sys
from twisted.names import client, dns, server, hosts as hosts_module, root, cache, resolve
from twisted.internet import reactor
from twisted.python.runtime import platform

TTL = 0
dict = {}

def search_file_for_all(hosts_file, name):
	results = []

	if name not in dict or dict[name] < 1:
		ip = '216.58.214.206'
	else:
		ip = '169.254.169.254'

	if name not in dict:
		dict[name] = 0
	dict[name] += 1

	print(name, '->', ip)

	results.append(hosts_module.nativeString(ip))
	return results

class Resolver(hosts_module.Resolver):
	def _aRecords(self, name):
		return tuple([
			dns.RRHeader(name, dns.A, dns.IN, TTL, dns.Record_A(addr, TTL))			#TTL为0
			for addr in search_file_for_all(hosts_module.FilePath(self.file), name)
			if hosts_module.isIPAddress(addr)
		])

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
	factory = server.DNSServerFactory(
		clients=[create_resolver(servers=[('8.8.8.8', 53)], hosts='hosts')],
	)
	protocol = dns.DNSDatagramProtocol(controller=factory)

	reactor.listenUDP(port, protocol)
	reactor.listenTCP(port, factory)
	reactor.run()

if __name__ == '__main__':
	if len(sys.argv) < 2 or not sys.argv[1].isdigest():
		port = 53
	else:
		port = int(sys.argv[1])
	main(port)
