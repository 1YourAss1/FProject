const http = require('http');
const fs = require("fs");

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
    
    switch (req.method) {
        case 'GET':
            res.statusCode = 200;
            res.setHeader('Access-Control-Allow-Origin', '*');
            fs.readFile("index.html", (error, data) => res.end(data));
            break;
        case 'POST':
            let data = '';
            req.on('data', (chunk) => data += chunk);
            req.on('end', () => console.log(data));
            break;
        default:
            res.statusCode = 400;
            res.end("Error");
            break;
    }
});

server.listen(port, hostname, () => {
    console.log(`Fingerprint server running at http://${hostname}:${port}/`);
});