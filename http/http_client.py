import http.client
import logging
import json
from time import sleep

logging.basicConfig(level=logging.DEBUG,
                    format='(%(asctime)-10s) %(message)s',
                    )

def printResponse(resp):
    logging.debug('{} {} {}'.format(resp._method, resp.status, resp.reason))
    print(resp.read().decode('utf-8'))


http_server = '127.0.0.1:8000'
# create a connection
conn = http.client.HTTPConnection(http_server)

# GET index
conn.request('GET', '/')
resp = conn.getresponse()
printResponse(resp)
sleep(2.0)

# GET recurso no existente
conn.request('GET', '/noexiste.html')
resp = conn.getresponse()
printResponse(resp)
sleep(2.0)

# HEAD index
conn.request('HEAD', '/index.html')
resp = conn.getresponse()
printResponse(resp)
print(resp.headers)
sleep(2.0)

# POST json
header = {'Content-type': 'application/json'}
info = {'variable': 'valor'}
json_data = json.dumps(info)
conn.request('POST', '/', json_data, header)
resp = conn.getresponse()
printResponse(resp)
sleep(1.0)

# DELETE index
conn.request('DELETE', '/')
resp = conn.getresponse()
printResponse(resp)
sleep(1.0)

# DELETE archivo de texto
conn.request('DELETE', '/a.txt')
resp = conn.getresponse()
printResponse(resp)
sleep(2.0)

conn.request('DELETE', '/a.txt')
resp = conn.getresponse()
printResponse(resp)
sleep(2.0)

# PUT crea archivo json
header = {'Content-type': 'application/json'}
info = {'variable': 'valor'}
json_data = json.dumps(info)
conn.request('PUT', '/', json_data, header)
resp = conn.getresponse()
printResponse(resp)
sleep(2.0)

# No implementados
conn.request('CONNECT', '/')
resp = conn.getresponse()
printResponse(resp)
sleep(1.0)

conn.request('TRACE', '/')
resp = conn.getresponse()
printResponse(resp)
sleep(1.0)

conn.request('OPTIONS', '/')
resp = conn.getresponse()
printResponse(resp)
sleep(1.0)

conn.close()