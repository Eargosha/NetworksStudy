import socket

IP_DONTFRAGMENT = 14  # Для Windows


def send_data(host, port, data, df_flag):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.IPPROTO_IP, IP_DONTFRAGMENT, df_flag)

    try:
        sock.sendto(data, (host, port))
        print(f"Sent {len(data)} bytes. DF={df_flag}")
    except OSError as e:
        print(f"Error: {e}")
    finally:
        sock.close()


# Тестовые данные для фрагментации (1600 байт данных):
data_size = 60000  # Размер данных
data = b'A' * data_size
server_host = '192.168.0.8'  # Используйте реальный IP, а не loopback
server_port = 9999

send_data(server_host, server_port, data, df_flag=0)
