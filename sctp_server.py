import socket
import sctp

host = socket.gethostname()
port = 1234

sock = sctp.sctpsocket_tcp(socket.AF_INET)
sock.bind((host, port))
sock.listen(5)

while True:

    print ('waiting for a connection')
    connection, client_address = sock.accept()
    while True:
        data = connection.recv(200)
        print (data.rstrip())

connection.close()
