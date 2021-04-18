from __future__ import print_function
a=int(raw_input("Enter Total Inputs : "))
l=[""]*a
n=0
while n<a:
	b=int(raw_input("Enter Value :"))
	c=int(raw_input("Enter Value :"))
	d=int(raw_input("Enter Value :"))
	if (b<c) and (b<d):
		l[n]=b
	elif (c<b) and (c<d):
		l[n]=c
	elif (d<b) and (d<c):
		l[n]=d
	else:
		print("Equal/Invalid")
	n+=1
print("Smaller numbers are :",l)