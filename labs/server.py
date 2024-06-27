import socket
s = socket.socket()
s.bind(("127.0.0.1", 12345))
s.listen()
while True:
    c, addr = s.accept() # Establish connection with client.
    print("Got connection from", addr)
    client_msg = c.recv(1024)
    print('Received:' + client_msg.decode())
    server_msg = "Thank you for connecting"
    c.send(server_msg.encode())
    c.close()
