from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 5555

class FingerprintServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        with open("index.html") as index:
            self.wfile.write(bytes(index.read(), "utf-8"))
    
    def do_POST(self):
        length = int(self.headers.get('content-length'))
        data = self.rfile.read(length)
        print(data)

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), FingerprintServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")