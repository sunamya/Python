from __future__ import print_function
a=int(raw_input("Enter Total Inputs : "))
l=[""]*a
n=0
while n<a:
	b=int(raw_input("Enter Value :"))
	c=int(raw_input("Enter Value :"))
	if b<c:
		l[n]=b
	else:
		l[n]=c
	n+=1
print("Smaller numbers are :",l)
