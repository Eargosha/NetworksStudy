import socket


def run_server():
    # Создаем UDP-сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Привязываем сокет к адресу и порту
    server_socket.bind(('', 9999))
    print("Server is listening on port 9999")

    try:
        while True:
            # Принимаем данные и адрес отправителя
            data, addr = server_socket.recvfrom(65536)  # Максимальный размер UDP-пакета
            print(f"Received {len(data)} bytes from {addr}")
    except KeyboardInterrupt:
        # Обработка прерывания (Ctrl+C)
        print("Server stopped.")
    finally:
        # Закрываем сокет при завершении
        server_socket.close()


run_server()
