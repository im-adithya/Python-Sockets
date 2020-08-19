import socket

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 1234

ss.bind((host,port))
ss.listen(5)

while True:
    cs, address = ss.accept()

    print('received connection from: %s ' % str(address))
    message = 'Now I get it'

    cs.send(message.encode('ascii'))
    cs.close()