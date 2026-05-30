import http.server
import socketserver
import urllib.parse
import os

PORT = 3000
DIRECTORY = "."

class RewriteHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        
        # Handle /career-detail/NAME -> career-details.html?name=NAME
        if parsed.path.startswith('/career-detail/'):
            name = parsed.path.split('/')[-1]
            self.path = f'/career-details.html?name={name}'
        
        # If no extension, try adding .html for clean URL support
        elif not os.path.splitext(parsed.path)[1] and parsed.path != '/':
            potential_file = parsed.path.lstrip('/') + '.html'
            if os.path.exists(potential_file):
                self.path = potential_file

        return super().do_GET()

os.chdir(DIRECTORY)
with socketserver.TCPServer(("", PORT), RewriteHandler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()
