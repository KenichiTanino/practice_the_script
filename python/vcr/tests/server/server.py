from datetime import datetime
from xmlrpc.client import DateTime
from xmlrpc.server import SimpleXMLRPCServer
 
 
def hello(message):
    # Heloo {}返却
    return 'Hello {}.'.format(message)
 
 
def time_result():
    # 時刻返却
    return DateTime(datetime.now())
 
 
server = SimpleXMLRPCServer(('localhost', 8889))
 
server.register_function(hello, 'hello')
server.register_function(time_result, 'time_result')
 
server.register_introspection_functions()
 
print("start server")
server.serve_forever()
