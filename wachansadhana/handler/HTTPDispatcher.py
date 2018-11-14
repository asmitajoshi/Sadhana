import sys
import os
import http.server
import socketserver

def module_name(instance):
  return instance.__module__ + '.' + instance.__class__.__name__

def start_server():
  HandlerClass = http.server.SimpleHTTPRequestHandler
  with socketserver.TCPServer(("", PORT), HandlerClass) as httpd:
    print(module_name(httpd), " serving at port ", PORT)
    httpd.serve_forever()

def main():
  pwd = os.getcwd()
  try:
    os.chdir('/var/www/')
    start_server()
  finally:
    os.chdir(pwd)

PORT = 8000
if __name__ == "__main__":
  main()

