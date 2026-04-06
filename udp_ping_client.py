import socket
import time

HOST = '127.0.0.1'
PORT = 5555
BUFFER_SIZE = 1024
PING_COUNT = 10

def run_client():
    """UDP клиент для отправки пингов и измерения времени ответа"""
    print("[КЛИЕНТ] Запуск UDP клиента...")
    print(f"[КЛИЕНТ] Отправка {PING_COUNT} пакетов на {HOST}:{PORT}\n")
    
    # Создание UDP сокета
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Устанавливаем таймаут для получения ответа
    client_socket.settimeout(2.0)
    
    total_time = 0
    successful_pings = 0
    
    try:
        for i in range(1, PING_COUNT + 1):
            # Формирование сообщения с таймштампом
            timestamp = time.time()
            message = f"ping {i} {timestamp}"
            
            try:
                # Отправка сообщения
                client_socket.sendto(message.encode('utf-8'), (HOST, PORT))
                send_time = time.time()
                
                # Получение ответа
                response, _ = client_socket.recvfrom(BUFFER_SIZE)
                receive_time = time.time()
                
                # Расчет времени ответа (round-trip time)
                rtt = (receive_time - send_time) * 1000  # в миллисекундах
                total_time += rtt
                successful_pings += 1
                
                print(f"[ОТВЕТ] пакет={i} время={rtt:.3f}мс от {HOST}:{PORT}")
            
            except socket.timeout:
                print(f"[ТАЙМАУТ] пакет={i} - нет ответа от сервера")
            
            # Небольшая задержка между отправками
            time.sleep(0.1)
    
    finally:
        # Вывод статистики
        print("\n[СТАТИСТИКА]")
        print(f"Отправлено пакетов: {PING_COUNT}")
        print(f"Получено ответов: {successful_pings}")
        print(f"Потеряно пакетов: {PING_COUNT - successful_pings}")
        
        if successful_pings > 0:
            avg_time = total_time / successful_pings
            print(f"Среднее время ответа: {avg_time:.3f}мс")
            print(f"Общее время: {total_time:.3f}мс")
        
        client_socket.close()
        print("[КЛИЕНТ] Соединение закрыто")

if __name__ == "__main__":
    run_client()
