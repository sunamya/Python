from __future__ import print_function
a=int(raw_input("Enter Length : "))
l=[""]*a
n=0
while n<a:
	l[n]=int(raw_input("Enter Value : "))
	n+=1
min=l[0]
max=l[0]
print("Array is : ",l)
n=0
while (n<a):
	if (l[n]<min):
			min=l[n]
	n+=1
n=0
while n<a:
	if (l[n]>max):
		max=l[n]
	n+=1
print("Minimum No. is : ",min)
print("Maximum No. is : ",max)