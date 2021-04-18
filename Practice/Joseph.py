from __future__ import print_function
a=int(raw_input("Enter Range : "))
b=int(raw_input("Enter Interval : "))
l=range(1,a+1)
print("Number is : ",l)
n=0
while len(l)>1:
	print(len(l))
	n+=1
	if len(l)<b:
		while len(l)>1:
			del l[len(l)-1]
			print(l)
		break
	if len(l)<(b*n):
		n=1
		del l[(b*n)-1]
		print(l)
	else:
		del l[(b*n)-1]
		print(l)
print("Number is : ",l)

