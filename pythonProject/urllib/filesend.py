import socket

host="localhost"
port=6767

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
print("Server is listening")
s.listen(1)
c,addr=s.accept()
filename = c.recv(1024)
try:
    f=open(filename,"rb")
    content=f.read()
    c.send(content)
    f.close()
except FileNotFoundError:
    c.send(b"File not found")


c.close()