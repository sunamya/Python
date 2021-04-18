from __future__ import print_function
a=int(raw_input("Enter total No. of Data : "))
l=[""]*a
n=0
while n<a:
	b=int(raw_input("Enter value : "))
	c=int(raw_input("Enter value : "))
	sum=b+c
	l[n]=sum
	n+=1
print('Sum : ',l)