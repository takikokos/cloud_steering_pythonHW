#!/usr/bin/python3
import socket
from threading import Thread
import sys


MAIN_TCP_PORT = 8000
MY_IP = '127.0.0.1'
FREE_TCP_PORT = 5005
BUFFER_SIZE = 1024
TIMEOUT = 0.5 # 0.5 sec
WELCOME_MESSAGE = "Welcome, {}!\nThere are following commands :\n!quit - leave chat\n\
!members - get all users\n!user_name msg - send msg to user_name\n!all msg - send msg to all users (set as default behaviour)\n"


class HandleConnection(Thread):
    active_connections = []

    def __init__(self, tcp_port, user_name):
        Thread.__init__(self)
        self.user_name = user_name
        self.new_messages = []
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((MY_IP, tcp_port))
        self.tcp_port = tcp_port
        self.socket.listen(1)
        self.connection, self.address = self.socket.accept()
        print(f"Connection with {self.address} established")
        self.connection.settimeout(TIMEOUT)

    def main(self):
        try:
            msg = self.connection.recv(BUFFER_SIZE).decode().rstrip()
        except:
            # check for new messages and return
            for author, msg in self.new_messages:
                self.connection.send(f"(from '{author}') {msg}\n".encode())
            self.new_messages = []
            return True
        if msg == "!quit":
            return False
        elif msg == "!members":
            # get all chat members
            ans = ""
            for t in HandleConnection.active_connections:
                ans += t.user_name
                ans += ", "
            ans = ans.rstrip(", ") + "\n"
            self.connection.send(ans.encode())
        elif msg.startswith("!all"):
            # send message to all
            msg = msg.lstrip("!all ")
            for t in HandleConnection.active_connections:
                t.new_messages.append((self.user_name, msg)) # send to ALL (even myself)
        elif msg.startswith("!"):
            # send direct message
            # will send to ALL users with such name
            to_user = msg[1:].split()[0]
            msg = " ".join(msg[1:].split()[1:])
            sent = False
            for t in HandleConnection.active_connections:
                if t.user_name == to_user:
                    t.new_messages.append((self.user_name, msg))
                    sent = True
            if not sent:
                self.connection.send(f"No user with name {to_user}\n".encode())
        else:
            # default send mesage to all
            for t in HandleConnection.active_connections:
                if t != self:
                    t.new_messages.append((self.user_name, msg))
        return True
    
    def run(self):
        # send service message to all about new user in chat
        for t in HandleConnection.active_connections:
            t.new_messages.append(("SERVER", f"{self.user_name} connected to chat\n"))

        HandleConnection.active_connections.append(self)
        self.connection.send(WELCOME_MESSAGE.format(self.user_name).encode())
        # main loop
        while self.main():
            pass
        self.connection.close()
        print(f"Connection with {self.address} closed")
        HandleConnection.active_connections.remove(self)

        # send service message to all about user leaving the chat
        for t in HandleConnection.active_connections:
            t.new_messages.append(("SERVER", f"{self.user_name} disconnected from chat\n"))


main_tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_tcp_socket.bind((MY_IP, MAIN_TCP_PORT))
while True:
    try:
        print(f"Server awaiting request on port : {MAIN_TCP_PORT}")
        main_tcp_socket.listen(1)
        connection, addr = main_tcp_socket.accept()
        print(f"Got request for connection from {addr}")
        user_name = connection.recv(BUFFER_SIZE).decode().strip()
        connection.send(str(FREE_TCP_PORT).encode())
        connection.close()

        FREE_TCP_PORT += 1
        thread = HandleConnection(FREE_TCP_PORT - 1, user_name)
        thread.daemon = True
        thread.start()
    except (KeyboardInterrupt, SystemExit):
        print("Closing all the connections and stoping threads...")
        for t in HandleConnection.active_connections:
            t.connection.close()
            t.socket.close()
            t._stop()
            print("Done")
        print("Exit")
        sys.exit()    
    