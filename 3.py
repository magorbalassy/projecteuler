import math;

def isPrime(a):
	prime=True
	for i in range(2,int(math.sqrt(a))):
		if a%i==0: prime=False
	return prime


div=[];
nr=600851475143
prime=True
for i in range (1,int(math.sqrt(600851475143))):
	if nr%i==0: div.append(i)
div.append(64)
for i in div:
	print i, ":", isPrime(i)