import pickle
import socket
import threading

def receive_msg(socket):
    while True:
        response = pickle.loads(socket.recv(100))
        print(f"{response[0]}:'{response[1]}'")

def send_msg(socket):
    while True:
        user_input = input()
        socket.send(pickle.dumps(user_input))

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(('localhost',8080))

name = print('enter name')
send_msg(client_socket)

thread_1 = threading.Thread(target=receive_msg,args=(client_socket))
thread_2 = threading.Thread(target=send_msg,args=(client_socket))
thread_1.start()
thread_2.start()