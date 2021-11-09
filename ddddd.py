import socketserver
import http.server
import ssl

httpd = socketserver.TCPServer(('0.0.0.0', 10000), http.server.SimpleHTTPRequestHandler)

httpd.socket = ssl.wrap_socket(httpd.socket, certfile=("/root/Desktop/server.pem"), keyfile="/root/Desktop/server.key", server_side=True)

httpd.serve_forever()