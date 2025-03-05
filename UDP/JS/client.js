const dgram = require('dgram');
const client = dgram.createSocket('udp4');

// Параметры отправки
const SERVER_HOST = '192.168.0.8'; // Замените на IP сервера
const SERVER_PORT = 9999;
const DATA_SIZE = 65000; // Размер данных
const data = Buffer.alloc(DATA_SIZE, 'A'); // Создание данных

// Отправка данных
client.send(data, SERVER_PORT, SERVER_HOST, (err) => {
    if (err) {
        console.error('Error:', err);
        // Если пакет слишком большой для MTU и DF=1, будет ошибка "EMSGSIZE"
        if (err.code === 'EMSGSIZE') {
            console.log('Packet too large for MTU (DF is set?)');
        }
    } else {
        console.log(`Successfully sent ${data.length} bytes.`);
    }
    client.close();
});