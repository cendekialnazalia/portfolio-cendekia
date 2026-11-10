# Local dev server for the portfolio: serves ./site and tells the browser not to cache,
# so every reload shows the latest edits.
import functools, http.server, os

PORT = 5173
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")


class NoCache(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, must-revalidate")
        self.send_header("Expires", "0")
        super().end_headers()


if __name__ == "__main__":
    handler = functools.partial(NoCache, directory=ROOT)
    with http.server.ThreadingHTTPServer(("", PORT), handler) as httpd:
        print(f"Serving {ROOT} at http://localhost:{PORT}")
        httpd.serve_forever()
