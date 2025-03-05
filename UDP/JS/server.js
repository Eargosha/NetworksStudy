const dgram = require('dgram');

const server = dgram.createSocket('udp4');

server.on('message', (msg, rinfo) => {
    console.log(`Received ${msg.length} bytes from ${rinfo.address}:${rinfo.port}`);
});

server.on('listening', () => {
    const address = server.address();
    console.log(`Server is listening on ${address.address}:${address.port}`);
});

server.bind(9999);