#!/usr/local/bin/python3

import http.server
import socketserver
import json
import sys

# Define your JSON data
#filename = sys.argv[0]
with open("data.json", "r") as data:
    json_data = data.read()

# Define the HTTP request handler
class JSONHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Set the response headers
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        # Send the JSON data as the response
        self.wfile.write(json_data.encode('utf-8'))

# Set the port for the server
port = 8000

# Create the HTTP server with the custom request handler
with socketserver.TCPServer(("", port), JSONHandler) as httpd:
    print(f"Serving at port {port}")
    httpd.serve_forever()
