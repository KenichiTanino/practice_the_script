from datetime import datetime
from xmlrpc.client import ServerProxy


def xmlrpc_client_hello():
    proxy = ServerProxy('http://localhost:8889/')
 
    l = proxy.system.listMethods()
    hello_message = proxy.hello('World')
    return dict(list=l, hello_message=hello_message)


def xmlrpc_client_time_result():
    proxy = ServerProxy('http://localhost:8889/')

    return proxy.time_result()
