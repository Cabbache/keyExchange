import socket, time
from random import randint
import Crypto

def send(conn, msg):
	conn.send(msg.encode('utf-8'))
	print("sent >> " + str(msg))

print("(g^a mod p)^b mod p = (g^b mod p)^a mod p")

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

addr = "127.0.0.1" #you may change this
port = 31415 #you may change this

# Connect the socket to the port where the server is listening
server_address = (addr, port)
print('connecting to %s port %s' % server_address)

sock.connect(server_address)
print("connected")

req = sock.recv(5).decode('utf-8')
if req == "hello":
	print("got hello")
	send(sock,"hello")
else:
	print("got "+str(req))
	print("protocol mismatch")
g = int(sock.recv(10))
print("got g = "+str(g))
send(sock,"ok")
p = int(sock.recv(10))
print("got p = "+str(p))
priKey = randint(400, 800)
print("generated private key = "+str(priKey))
pubKey = Crypto.genKey(g,p,priKey)
print("Generated public key "+str(pubKey))
IpubKey = int(sock.recv(500))
print("recieved key "+str(IpubKey))
send(sock,str(pubKey))
key = Crypto.genKey(IpubKey,p,priKey)
print("Agreed on secret key >> "+str(key)+" << ")
sock.close()
input("END") #for noob windows users that see flashing black window
