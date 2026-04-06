import socket

def send_http_request():
    """Отправка HTTP-запроса к google.com через сокет"""
    
    # Параметры сервера
    HOST = 'google.com'
    PORT = 80
    
    print(f"[ЗАПРОС] Подключение к {HOST}:{PORT}...\n")
    
    try:
        # Создание сокета
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Установка таймаута
        sock.settimeout(10)
        
        # Подключение к серверу
        sock.connect((HOST, PORT))
        print(f"[УСПЕХ] Подключено к {HOST}\n")
        
        # Формирование HTTP-запроса
        http_request = (
            "GET / HTTP/1.1\r\n"
            "Host: google.com\r\n"
            "User-Agent: Python/3.x Socket Client\r\n"
            "Connection: close\r\n"
            "\r\n"
        )
        
        # Отправка запроса
        print("[ОТПРАВКА] HTTP-запрос:")
        print("-" * 50)
        print(http_request)
        print("-" * 50)
        
        sock.sendall(http_request.encode('utf-8'))
        
        # Получение ответа
        print("\n[ПОЛУЧЕНИЕ] HTTP-ответ:")
        print("-" * 50)
        
        response = b""
        while True:
            try:
                chunk = sock.recv(4096)
                if not chunk:
                    break
                response += chunk
            except socket.timeout:
                break
        
        # Декодирование и вывод ответа
        response_str = response.decode('utf-8', errors='replace')
        print(response_str)
        
        print("-" * 50)
        print(f"\n[УСПЕХ] Получено {len(response)} байт")
        
        sock.close()
        print("[ЗАКРЫТО] Соединение разорвано")
    
    except socket.gaierror as e:
        print(f"[ОШИБКА] Не удалось разрешить имя хоста: {e}")
    except socket.error as e:
        print(f"[ОШИБКА] Ошибка сокета: {e}")
    except Exception as e:
        print(f"[ОШИБКА] Неожиданная ошибка: {e}")

if __name__ == "__main__":
    send_http_request()
