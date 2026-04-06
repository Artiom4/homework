import socket
import os
from pathlib import Path

def run_server(port=8000):
    print(f"Working directory: {os.getcwd()}")
    print(f"Files in directory: {os.listdir('.')}\n")
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server_socket.bind(('127.0.0.1', port))
        server_socket.listen(1)
        print(f"Server started on http://127.0.0.1:{port}\n")
    except Exception as e:
        print(f"Error: {e}")
        return

    try:
        while True:
            print("Waiting for connection...")
            client_socket, addr = server_socket.accept()
            print(f"Connected from {addr}")
            
            try:
                request = client_socket.recv(1024).decode('utf-8')
                request_line = request.split('\r\n')[0]
                method, path, protocol = request_line.split(' ')
                print(f"Requested: {method} {path}")
                
                # Игнорируем favicon
                if path == '/favicon.ico':
                    response = b"HTTP/1.1 404 Not Found\r\n\r\n"
                    client_socket.sendall(response)
                    client_socket.close()
                    print("Favicon ignored\n")
                    continue
                
                if path == '/':
                    path = 'index.html'
                else:
                    path = path.lstrip('/')
                
                file_path = Path(path)
                print(f"Looking for: {file_path}")
                
                if file_path.exists() and file_path.is_file():
                    if path.endswith('.css'):
                        content_type = 'text/css; charset=utf-8'
                    elif path.endswith('.html'):
                        content_type = 'text/html; charset=utf-8'
                    else:
                        content_type = 'text/plain; charset=utf-8'
                    
                    with open(file_path, 'rb') as f:
                        content = f.read()
                    
                    print(f"✓ Sending 200 OK for {path}\n")
                    response = (
                        f"HTTP/1.1 200 OK\r\n"
                        f"Content-Type: {content_type}\r\n"
                        f"Content-Length: {len(content)}\r\n"
                        f"Connection: close\r\n"
                        f"\r\n"
                    ).encode() + content
                else:
                    print(f"✗ File not found: {path}\n")
                    error_msg = b"<h1>404 Not Found</h1>"
                    response = (
                        f"HTTP/1.1 404 Not Found\r\n"
                        f"Content-Type: text/html; charset=utf-8\r\n"
                        f"Content-Length: {len(error_msg)}\r\n"
                        f"Connection: close\r\n"
                        f"\r\n"
                    ).encode() + error_msg
                
                client_socket.sendall(response)
            finally:
                client_socket.close()
    except KeyboardInterrupt:
        print("\nServer stopped")
    finally:
        server_socket.close()

if __name__ == '__main__':
    run_server()