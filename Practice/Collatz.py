from __future__ import print_function
a=int(raw_input("Enter Sequence No. : "))
n=0
l=[]
f=[]
while n<a:
	k=int(raw_input("Enter Value : "))
	l.append(k)
	n+=1
n=0
while n<a:
	x=l[n]
	count=0
	while x>1:
		if x%2==0:
			x=x/2
		else:
			x=(3*x)+1
		count+=1
	f.append(count)
	n+=1
print("Sequence : ",f)
