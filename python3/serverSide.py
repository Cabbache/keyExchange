#(g^a % p)^b % p = (g^b % p)^a % p
import socket, time, math
from random import randint
import Crypto

def send(conn, msg):
	conn.send(msg.encode('utf-8'))
	print("sent >> " + str(msg))

print("(g^a mod p)^b mod p = (g^b mod p)^a mod p")

HOST = '0.0.0.0' #you may change this
PORT = 31415 #you may change this

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print("Socket created")

try:
	s.bind((HOST, PORT))
except socket.error as msg:
	print("CRITICAL: Bind failed. Error Code : " + str(msg[0]) + " Message " + msg[1])

print("Socket bind complete")
s.listen(10)
print("Socket now listening")
print("Waiting for connections")

conn, addr = s.accept()
send(conn, "hello")

req = conn.recv(5).decode('utf-8')

if req != "hello":
	print("protocol mismatch")
else:
	print("got hello")
g = Crypto.genRandPrime()
p = Crypto.genRandPrime()
print("Generated g = "+str(g))
print("Generated p = "+str(p))
send(conn, str(g))
conn.recv(2)
send(conn, str(p))
priKey = randint(400, 800)
print("Generated private key = "+str(priKey))
pubKey = Crypto.genKey(g,p,priKey)
print("generated public key "+str(pubKey))
send(conn, str(pubKey))
IpubKey = int(conn.recv(500))
print("recieved key "+str(IpubKey))
key = Crypto.genKey(IpubKey,p,priKey)
print("Agreed on secret key >> "+str(key)+" <<")
s.close()
input("END") #for noob windows users that see flashing black window
