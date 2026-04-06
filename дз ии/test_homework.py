#!/usr/bin/env python3
"""
Тестирование всех четырех домашних заданий
"""

import os
import sys

print("=" * 60)
print("ПРОВЕРКА ДОМАШНИХ ЗАДАНИЙ")
print("=" * 60)

# 1. Проверка TCP-чата
print("\n[1] TCP-ЧАТ (one_file_tcp.py)")
print("-" * 60)
if os.path.exists("one_file_tcp.py"):
    with open("one_file_tcp.py", "r", encoding="utf-8") as f:
        content = f.read()
        has_server = "def server()" in content
        has_client = "def client()" in content
        has_while = "while True:" in content
        has_messages = "client_socket.recv" in content and "client_socket.send" in content
        
    status = "✓ ОК" if (has_server and has_client and has_while) else "✗ ОШИБКА"
    print(f"{status} Найдены функции server() и client(): {has_server and has_client}")
    print(f"{'✓' if has_while else '✗'} Цикл while True для обмена сообщениями: {has_while}")
    print(f"{'✓' if has_messages else '✗'} Отправка/получение сообщений: {has_messages}")
else:
    print("✗ Файл не найден")

# 2. Проверка mini_http.py
print("\n[2] HTTP-СЕРВЕР (mini_http.py)")
print("-" * 60)
if os.path.exists("mini_http.py"):
    with open("mini_http.py", "r", encoding="utf-8") as f:
        content = f.read()
        has_css_check = "endswith('.css')" in content
        has_content_type = "Content-Type: text/css" in content or "'text/css'" in content
        has_socket = "socket.socket" in content
        has_recv = "recv(" in content or "recvfrom(" in content
        
    status = "✓ ОК" if (has_css_check and has_content_type) else "✗ ОШИБКА"
    print(f"{status} Проверка расширения .css: {has_css_check}")
    print(f"{'✓' if has_content_type else '✗'} Отправка Content-Type: text/css: {has_content_type}")
    print(f"{'✓' if has_socket else '✗'} Использование сокета: {has_socket}")
    
    if os.path.exists("style.css"):
        print(f"✓ Файл style.css существует")
    else:
        print(f"✗ Файл style.css не найден")
else:
    print("✗ Файл не найден")

# 3. Проверка UDP-пинга
print("\n[3] UDP-ПИНГ")
print("-" * 60)
has_server = os.path.exists("udp_ping_server.py")
has_client = os.path.exists("udp_ping_client.py")

print(f"{'✓' if has_server else '✗'} Сервер (udp_ping_server.py): {has_server}")
print(f"{'✓' if has_client else '✗'} Клиент (udp_ping_client.py): {has_client}")

if has_client:
    with open("udp_ping_client.py", "r", encoding="utf-8") as f:
        content = f.read()
        has_timestamp = "time.time()" in content
        has_10_pings = "PING_COUNT = 10" in content
        has_rtt = "rtt" in content or "round-trip" in content.lower()
        
    print(f"{'✓' if has_timestamp else '✗'} Использование time.time() для таймштампа: {has_timestamp}")
    print(f"{'✓' if has_10_pings else '✗'} Отправление 10 сообщений: {has_10_pings}")
    print(f"{'✓' if has_rtt else '✗'} Расчет времени ответа (RTT): {has_rtt}")

if has_server:
    with open("udp_ping_server.py", "r", encoding="utf-8") as f:
        content = f.read()
        has_echo = "sendto" in content and "recvfrom" in content
        
    print(f"{'✓' if has_echo else '✗'} Сервер отправляет сообщения обратно: {has_echo}")

# 4. Проверка HTTP-запроса через сокет
print("\n[4] HTTP-ЗАПРОС К GOOGLE.COM (http_request_socket.py)")
print("-" * 60)
if os.path.exists("http_request_socket.py"):
    with open("http_request_socket.py", "r", encoding="utf-8") as f:
        content = f.read()
        has_socket = "socket.socket" in content
        has_connect = ".connect(" in content
        has_google = "google.com" in content
        has_http = "GET /" in content or "HTTP/1.1" in content
        has_sendall = "sendall(" in content
        no_requests = "import requests" not in content
        
    status = "✓ ОК" if (has_socket and has_connect and has_google and has_http) else "✗ ОШИБКА"
    print(f"{status} Использование socket.socket: {has_socket}")
    print(f"{'✓' if has_connect else '✗'} Подключение к google.com: {has_connect and has_google}")
    print(f"{'✓' if has_http else '✗'} HTTP-запрос (GET, HTTP/1.1): {has_http}")
    print(f"{'✓' if has_sendall else '✗'} Отправка запроса (sendall): {has_sendall}")
    print(f"{'✓' if no_requests else '✗'} Без использования requests: {no_requests}")
else:
    print("✗ Файл не найден")

print("\n" + "=" * 60)
print("ОБЩАЯ ИНФОРМАЦИЯ")
print("=" * 60)
print(f"Рабочая директория: {os.getcwd()}")
print(f"Файлы в папке: {', '.join(sorted([f for f in os.listdir('.') if f.endswith('.py') or f.endswith('.css')]))}")
print("\n" + "=" * 60)
