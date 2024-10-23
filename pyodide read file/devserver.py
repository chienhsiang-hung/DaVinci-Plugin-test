import json, os
import http.server
import socketserver

PORT = 5003

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_headers(self):
        self.send_response(200)
        self.send_header('content-type', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        self.send_header('access-control-allow-origin', '*')
        self.send_header('access-Control-Allow-Private-Network', 'true')
        self.send_header('access-control-allow-methods', 'GET, OPTIONS')
        self.end_headers()
    def do_OPTIONS(self):
        return self.do_headers()
    def do_GET(self):
        self.do_headers()
        with open('file_example_XLSX_10.xlsx', 'rb') as f:
            self.wfile.write(f.read())

with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    print("serving at port", PORT)
    print(f'current wd = {os.getcwd()}')
    httpd.allow_reuse_address = True
    httpd.allow_reuse_port = True
    httpd.serve_forever()
