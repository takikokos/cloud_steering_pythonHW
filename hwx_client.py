#!/usr/bin/python3
import socket
from threading import Thread
import sys

HISTORY = []
SERVER_MAIN_TCP_PORT = 8000
SERVER_IP = '127.0.0.1'
BUFFER_SIZE = 1024
TIMEOUT = 0.3
INPUT_MSG = "(from you) : "
STOP_RECV_THREAD = False
WORKING_SOCKET = None
USER_NAME = "New user"

def get_messages():
    global WORKING_SOCKET
    while not STOP_RECV_THREAD:
        try:
            ans = WORKING_SOCKET.recv(BUFFER_SIZE).decode()
            HISTORY.append(ans.rstrip())
            # clear screen
            print("\n" * 100) 
            # use such strange formatting to avoid problems with switching threads
            txt_before = "\n".join(HISTORY)
            print(f'{txt_before}\n{INPUT_MSG}', end="") 
        except:
            pass

def init_connection():
    global WORKING_SOCKET
    global USER_NAME
    print("Trying to conenct to server...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((SERVER_IP, SERVER_MAIN_TCP_PORT))
    sock.send(USER_NAME.encode())
    print("Recieving a working port...")
    working_port = int(sock.recv(BUFFER_SIZE).decode())
    sock.close()
    print("Establishing a connection...")
    WORKING_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    WORKING_SOCKET.connect((SERVER_IP, working_port))
    print("Connected\n")


if __name__ == "__main__":
    USER_NAME = input("Enter your nickname : ")
    init_connection()

    hello_msg = WORKING_SOCKET.recv(BUFFER_SIZE).decode()
    HISTORY.append(hello_msg)
    print(hello_msg)
    print()

    WORKING_SOCKET.settimeout(TIMEOUT)
    recv_thread = Thread(target=get_messages, daemon=True)
    recv_thread.start()
    
    inp = ""
    while inp != "!quit":
        inp = input(INPUT_MSG)
        HISTORY.append(f"{INPUT_MSG}{inp}")
        WORKING_SOCKET.send(inp.encode())
        
    STOP_RECV_THREAD = True
    recv_thread.join()
    WORKING_SOCKET.close()
    sys.exit()
