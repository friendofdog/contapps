import dns.resolver
import docker
import sys

resolver = dns.resolver.Resolver()
resolver.nameservers = ['127.0.0.1']
resolver.port = 1053
answer = resolver.query('friendofdog.com', 'TXT')
print(answer.response)

cid = sys.argv[1]
dr_client = docker.from_env()
server = dr_client.containers.get(cid)
server.stop()
