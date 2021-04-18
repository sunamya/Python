from __future__ import print_function
def primefactor(j):
	i=1
	count=0
	while(i<=j): #Calculating factors of that number
		k=0
		if(j%i==0):
			m=1
		while(m<=i): #Calculating prime factor
			if(i%m==0):
				k=k+1
				m=+1
			if(k==2):
				count+=1
	return count
def prime(a,b):
	c1=0
	for j in range(a,b+1):
		c=primefactor(j)
		l=len(str(j))
		if c==l:
			c1+=1
	return c1
n=int(input()) #No. of test cases
for i in range(n):
	data=input().split()
	data=[int(x) for x in data]
	a,b=data[0],data[1]
	c2=prime(a,b)
	print(c2)
