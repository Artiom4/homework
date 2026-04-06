import socket

HOST = '127.0.0.1'
PORT = 5555
BUFFER_SIZE = 1024

def run_server():
    """UDP сервер для эхо-отправки сообщений"""
    print("[СЕРВЕР] Запуск UDP сервера...")
    
    # Создание UDP сокета
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    
    print(f"[СЕРВЕР] Прослушивание на {HOST}:{PORT}")
    print("[СЕРВЕР] Ожидание сообщений...\n")
    
    try:
        while True:
            # Получение сообщения от клиента
            data, client_address = server_socket.recvfrom(BUFFER_SIZE)
            message = data.decode('utf-8')
            
            print(f"[ПОЛУЧЕНО] от {client_address}: {message}")
            
            # Отправка того же сообщения обратно
            server_socket.sendto(message.encode('utf-8'), client_address)
    
    except KeyboardInterrupt:
        print("\n[СЕРВЕР] Остановка сервера...")
    
    finally:
        server_socket.close()
        print("[СЕРВЕР] Соединение закрыто")

if __name__ == "__main__":
    run_server()
