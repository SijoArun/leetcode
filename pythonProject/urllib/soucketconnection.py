import socket

host="localhost"
port=4000

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
print("Server is listening")
s.listen(1)
c,addr=s.accept()
print("conection from :",str(addr))
c.send(b"Hi How are you")
c.send("bye".encode())
c.close()