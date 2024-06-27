import socket
s = socket.socket()
s.connect(('127.0.0.1', 12345))
msg = "Hello, Dr. Kim. This is Luis"
s.send(msg.encode())
print(s.recv(1024))
s.close()
