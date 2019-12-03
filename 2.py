f1=1
f2=2
sum=0
x=f2
while x<=4000000:
	if x%2==0: 
		sum+=x
	x=(f1 + f2)
	f1=f2
	f2=x
print sum
