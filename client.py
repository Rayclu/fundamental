import socket
import gamelib
def connect_to_server(host='10.58.193.22', port=8383):
    
    while True:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        print("connected.")
        if (input("quiere salir? <si, no>").lower() == "si"):
            break
        


connect_to_server()

