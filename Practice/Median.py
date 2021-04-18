from __future__ import print_function
a=int(raw_input("Enter No. Of Inputs : "))
c=a/2
l=[]
n=0
while n<a:
	s=[]
	m=0
	while m<a:
		k=int(raw_input("Enter Value : "))
		s.append(k)
		m+=1
	l.append(s)
	n+=1
print(l)
n=0
while n<a:
	l[n].sort()
	print(l[n])
	print("Median is : ",l[n][c])
	n+=1
		