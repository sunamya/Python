from __future__ import print_function
def random1(a):
	a=a**2
	a1=a
	count=0
	while a1>0:
		a1/=10
		count+=1
	if count<8:
		c=8-count
		a=a*(10**c)
	count=0
	new=0
	while a>0:
		b=a%10
		a/=10
		count+=1
		if count>2 and count<7:
			new+=b*(10**(count-3))
	return new
x=int(raw_input("Enter 4 digit value : "))
y=random1(x)
print("Random number is : ",y)