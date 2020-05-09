import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from io import BytesIO

hostName = "localhost"
serverPort = 8000

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            rootdir = os.path.dirname(os.path.realpath(__file__))
            if self.path is '/':                              # index.html
                f = open(rootdir + '/index.html')
            else:
                f = open(rootdir + self.path)                 # Abre el archivo

            self.send_response(200)                           # OK

            self.send_header('Content-type', 'text-html')     # Envía cabecera
            self.end_headers()

            self.wfile.write(f.read().encode())               # Envía el archivo
            f.close()
            return
        except IOError:
            self.send_error(404, 'No encontrado')             # No se encontró el archivo
            return

    def do_HEAD(self): # Retorna solo la cabecera del recurso
        try:
            rootdir = os.path.dirname(os.path.realpath(__file__))

            if self.path is '/':                              # index.html
                f = open(rootdir + '/index.html')
            else:
                f = open(rootdir + self.path)                 # Abre el archivo
            f.close
            self.send_response(200)                           # OK
            self.end_headers()
            return

        except IOError:
            self.send_error(404, 'No encontrado')                 # No se encontró el recurso

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        content_len = int(self.headers['Content-Length'])
        post_body = self.rfile.read(content_len)
        self.wfile.write('received post request: {}'.format(post_body).encode())

    def do_PUT(self):
        content_len = int(self.headers['Content-Length'])
        post_body = self.rfile.read(content_len)
        j = json.dumps(post_body.decode())
        print(j)

        with open('data.json', 'w') as outfile:
            json.dump(j, outfile)

        self.send_response(201)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        self.wfile.write('received post request: {}'.format(post_body).encode())

    def do_DELETE(self):
        try:
            rootdir = os.path.dirname(os.path.realpath(__file__))
            if self.path is '/' or self.path.endswith('index.html'):
                self.send_error(405)
                return
            f = open(rootdir + self.path)
            f.close()

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            os.remove(rootdir + self.path)
            self.wfile.write('Eliminado {} del servidor'.format(self.path).encode())
            return

        except IOError:
            self.send_error(404, 'no encontrado')

    def do_CONNECT(self):
        self.send_error(501)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        self.wfile.write(b'No hay opciones que mostrar')

    def do_OPTIONS(self):
        self.send_error(501)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        self.wfile.write(b'No hay opciones que mostrar')

    def do_TRACE(self):
        self.send_error(501)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        self.wfile.write(b'No hay opciones que mostrar')

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Servidor iniciado http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")