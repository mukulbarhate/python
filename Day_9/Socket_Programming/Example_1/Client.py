import socket

with socket.socket() as c:
    c.connect(("localhost",5000))
    name=input("Enter your name: ")
    c.send(bytes(name,'utf-8'))
    print(c.recv(1024).decode())        # capacity of data