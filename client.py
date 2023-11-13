import pickle
import socket
import threading

def receive_msg(socket):
    
    while True:
        response = pickle.loads(socket.recv(100))
        print(f"{response[0]}:'{response[1]}'")

def send_msg(socket):
    
    user_input = input()
    socket.send(pickle.dumps(user_input))
    print('sent')

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
name = print('enter name')
client_socket.connect(('localhost',8080))

while True:

    threading.Thread(target=receive_msg,args=(client_socket,)).start()
    send_msg(client_socket)


