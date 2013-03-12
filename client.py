import xmlrpclib
proxy = xmlrpclib.ServerProxy('http://localhost:9000', allow_none=True)
proxy.Stop()
