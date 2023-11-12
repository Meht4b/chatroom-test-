import pickle
import socket
import select

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server_socket.bind(('localhost',8080))

server_socket.listen()

print('listening')

socket_list = [server_socket]
client_list = {}

def broadcast(list,msg):
    print('broadcast')
    for socket in list:
        socket.send(pickle.dumps(msg))

def handle(conn):
    print('recvd')
    broadcast(client_list.keys(),pickle.loads(conn.recv(100)))
    print('broadcasted')

while True:

    read_socket,_,error_socket = select.select(socket_list,[],socket_list)

    for unread_socket in read_socket:
        if unread_socket == server_socket:
            conn,addr = unread_socket.accept()
            print(addr)
            client_list[conn]=pickle.loads(conn.recv(100))
            broadcast(client_list.keys(),f'{client_list[conn]} joined')

        else:
            print('laksdjlk')
            handle(unread_socket)

