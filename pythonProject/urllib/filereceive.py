import socket

s=socket.socket()
s.connect(("localhost",6767))

f=input("Enter the file name")
s.send(f.encode())
content=s.recv(1024)
print(content.decode())



s.close()