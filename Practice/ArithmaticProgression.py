from __future__ import print_function
a=int(raw_input("Enter A : "))
b=int(raw_input("Enter B : "))
c=int(raw_input("Upto Where = "))
n=0
l=[]
while n<c:
	tot=a+(n*b)
	l.append(tot)
	n+=1
print("List : ",l)