#(g^a % p)^b % p = (g^b % p)^a % p

import math
from random import randint

def genRandPrime():
	x = int(randint(100000,1000000))
	for j in range(x-13,x+13):
		if isPrime(j):
			return j
	return genRandPrime()

def isPrime(n):
	if n % 2 == 0:
		return False
	lim = math.sqrt(n)
	for x in range(3, int(math.ceil(lim))+1):
		if n % x == 0:
			return False
	return True

def power(base, pwr):
	if pwr == 0:
		return 1
	else:
		return power(base, pwr-1)*base

def genKey(g, p, a):
	print("calculating "+str(g)+"^"+str(a)+" mod "+str(p))
	return int(power(g, a) % p)
