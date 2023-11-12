import pickle
import socket
import select

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('localhost',8080))

server_socket.listen()

socket_list = [server_socket]

def handle(conn):
    pass

while True:

    read_socket,_,error_socket = select.select(socket_list,[],socket_list)

    for unread_socket in read_socket:
        if unread_socket == server_socket:
            conn,addr = unread_socket.accept()
        else:
            handle(unread_socket)

