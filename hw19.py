import socket


UDP_PORT = 5005
UDP_IP = "127.0.0.1"

MY_DNS = {
    "my.google.com" : "228.228.228.228",
}

def gethostbyname(name):
    if type(name) == type(b""):
        name = name.decode()
    name = name.rstrip()
    if name in MY_DNS:
        return MY_DNS[name]
    else:
        try:
            return socket.gethostbyname(name)
        except:
            return "Name or service not known"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
print(f"Open udp socket on port {UDP_PORT}")

while True:
    data, addr = sock.recvfrom(1024)
    print(f"Recieved \"{data.decode().rstrip()}\" from {addr[0]}:{addr[1]}")
    
    ip = gethostbyname(data)

    sock.sendto((ip + "\n").encode(), addr)
    print(f"Sent \"{ip}\" to {addr[0]}:{addr[1]}")