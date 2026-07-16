import os
from http.server import BaseHTTPRequestHandler, HTTPServer


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        mensaje = (
            "Workstation ejecutándose correctamente en "
            "Red Hat OpenShift sobre UBI."
        )

        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(mensaje.encode("utf-8"))


if __name__ == "__main__":
    puerto = int(os.environ.get("PORT", "8080"))
    servidor = HTTPServer(("0.0.0.0", puerto), RequestHandler)

    print(f"Servidor iniciado en el puerto {puerto}")
    servidor.serve_forever()
