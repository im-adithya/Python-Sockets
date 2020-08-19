import socket

cs = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostname()
port = 1234

cs.connect((host,port))

message = cs.recv(1024)
cs.close()

print(message.decode('ascii'))