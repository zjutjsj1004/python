from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import http.server

import socketserver

class Handler(http.server.BaseHTTPRequestHandler):

    def do_POST(self):
        try:
            data = json.loads(self.rfile.read(int(self.headers.get('Content-Length'))).decode())
        except (TypeError, json.JSONDecodeError, UnicodeDecodeError):
            self.send_response(400)
            return
        print(data)
        self.send_response(204)
        self.end_headers()

def run_server(port=8000):
    with socketserver.TCPServer(("", port), Handler) as httpd:
        print("serving at port", port)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print('exit')
        finally:
            httpd.server_close()

if __name__ == '__main__':
    run_server(8888)
