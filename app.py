import os
from http.server import BaseHTTPRequestHandler, HTTPServer


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        message = (
            "Workstation ejecutándose correctamente en "
            "Red Hat OpenShift sobre UBI."
        )

        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(message.encode("utf-8"))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    server = HTTPServer(("0.0.0.0", port), RequestHandler)

    print(f"Servidor iniciado en el puerto {port}")
    server.serve_forever()
