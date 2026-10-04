from http.server import BaseHTTPRequestHandler, HTTPServer
import json

HOST = "0.0.0.0"
PORT = 3001
BACKEND = "A"
MACHINE = "Mac 3"
ETAG = '"team1-home-v1"'


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.handle_home()
        elif self.path == "/api/status":
            self.handle_status()
        else:
            self.send_error(404, "Not Found")

    def handle_home(self):
        if self.headers.get("If-None-Match") == ETAG:
            self.send_response(304)
            self.send_header("X-Backend", BACKEND)
            self.send_header("Cache-Control", "public, max-age=30")
            self.send_header("ETag", ETAG)
            self.end_headers()
            return

        body = f"""
            <!DOCTYPE html>
            <html>
            <head><title>Backend {BACKEND}</title></head>
            <body>
                <h1>Backend {BACKEND} is running!</h1>
                <p>Served by {MACHINE}</p>
            </body>
            </html>
            """.encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("X-Backend", BACKEND)
        self.send_header("Cache-Control", "public, max-age=30")
        self.send_header("ETag", ETAG)
        self.end_headers()
        self.wfile.write(body)

    def handle_status(self):
        body = json.dumps({"backend": BACKEND, "status": "ok"}).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("X-Backend", BACKEND)
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    print(f"Backend {BACKEND} listening on port {PORT}")
    HTTPServer((HOST, PORT), Handler).serve_forever()
