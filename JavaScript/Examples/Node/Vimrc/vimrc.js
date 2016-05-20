const fs = require('fs')
const http = require('http');

const hostname = '127.0.0.1';
const port = 8080;

http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.end(fs.readFileSync('vimrc.html', 'utf-8'));
}).listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
});
