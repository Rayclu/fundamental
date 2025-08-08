import socket as sk
import sqlite3 as sq

def startServer(url='0.0.0.0', port=8383):
    serverSocket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    serverSocket.bind((url, port))
    serverSocket.listen(1)

    print(f"Listening in: {url}:{port}")

    while True:
        client_socket, address = serverSocket.accept()
        print(f'Connection from {address}')
        client_socket.sendall(b'Hello, client!')
        client_socket.close()

if __name__ == "__main__":
    startServer()
