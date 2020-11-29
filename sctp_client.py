import socket
import sctp

sk = sctp.sctpsocket_tcp(socket.AF_INET)
sk.connect((socket.gethostname(), 1234))


print("Sending Message")
while True:
	string1 = input(":")
	print(string1)
	sk.sctp_send(msg= string1)


sk.shutdown(0)


sk.close()
