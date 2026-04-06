import socket
import threading
import sys

# Параметры сервера
HOST = 'localhost'
PORT = 5000
BUFFER_SIZE = 1024

def server(auto_mode=False):
    """TCP сервер для обмена сообщениями"""
    print("[СЕРВЕР] Запуск сервера...")
    
    # Создание сокета сервера
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    
    print(f"[СЕРВЕР] Прослушивание на {HOST}:{PORT}")
    
    # Ожидание подключения клиента
    client_socket, client_address = server_socket.accept()
    print(f"[СЕРВЕР] Клиент подключился: {client_address}")
    
    try:
        # Цикл обмена сообщениями
        while True:
            # Получение сообщения от клиента
            message = client_socket.recv(BUFFER_SIZE).decode('utf-8')
            
            if not message or message.lower() == 'exit':
                print("[СЕРВЕР] Клиент отключился")
                break
            
            print(f"[КЛИЕНТ]: {message}")
            
            # Отправка ответного сообщения
            if auto_mode:
                response = f"Ответ на: {message}"
            else:
                response = input("[СЕРВЕР] Ваше сообщение: ")
            
            if response.lower() == 'exit':
                client_socket.send("exit".encode('utf-8'))
                break
            
            client_socket.send(response.encode('utf-8'))
    
    finally:
        client_socket.close()
        server_socket.close()
        print("[СЕРВЕР] Соединение закрыто")

def client():
    """TCP клиент для обмена сообщениями"""
    print("[КЛИЕНТ] Подключение к серверу...")
    
    # Создание сокета клиента
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Подключение к серверу
        client_socket.connect((HOST, PORT))
        print(f"[КЛИЕНТ] Подключено к {HOST}:{PORT}")
        
        # Цикл обмена сообщениями
        while True:
            # Отправка сообщения серверу
            message = input("[КЛИЕНТ] Ваше сообщение: ")
            if message.lower() == 'exit':
                client_socket.send("exit".encode('utf-8'))
                break
            
            client_socket.send(message.encode('utf-8'))
            
            # Получение ответного сообщения
            response = client_socket.recv(BUFFER_SIZE).decode('utf-8')
            
            if not response or response.lower() == 'exit':
                print("[КЛИЕНТ] Сервер отключился")
                break
            
            print(f"[СЕРВЕР]: {response}")
    
    finally:
        client_socket.close()
        print("[КЛИЕНТ] Соединение закрыто")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].lower() == 'server':
        auto_mode = '--auto' in sys.argv
        server(auto_mode)
    else:
        client()
