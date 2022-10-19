from http.server import BaseHTTPRequestHandler, HTTPServer
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
        data = self.rfile.read(length).decode('utf-8')
        cur.execute(f"INSERT INTO fingerprints(data) VALUES('{data}');")
        conn.commit()
        

if __name__ == "__main__":      
    cur.execute("""CREATE TABLE IF NOT EXISTS fingerprints(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
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