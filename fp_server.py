from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import sqlite3

hostName = "localhost"
serverPort = 5555

conn = sqlite3.connect('fingerprint.db')
cur = conn.cursor()

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
        data = parse_qs(self.rfile.read(length).decode('utf-8'))
        name = data.get('name')[0]
        fingerprint = data.get('fingerprint')[0]
        cur.execute(f"INSERT INTO fingerprints(id,data) VALUES('{name}','{fingerprint}');")
        conn.commit()

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(f"Success, thank you, {name}!", "utf-8"))
        

if __name__ == "__main__":      
    cur.execute("""CREATE TABLE IF NOT EXISTS fingerprints(
        id TEXT PRIMARY KEY,
        data TEXT);
        """)
    conn.commit()
    
    webServer = HTTPServer((hostName, serverPort), FingerprintServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")