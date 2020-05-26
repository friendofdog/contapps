import dns.resolver

resolver = dns.resolver.Resolver()
resolver.nameservers = ['127.0.0.1']
resolver.port = 1053
answer = resolver.query('friendofdog.com', 'TXT')
print(answer.response)
