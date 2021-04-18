from __future__ import print_function
a=int(raw_input("Enter No. of cases : "))
n=0
l=[]
while n<a:
	s=[]
	m=0
	while m==0:
		k=int(raw_input("Enter Kilometer : "))
		s.append(k)
		v1=int(raw_input("Enter speed 1 : "))
		s.append(v1)
		v2=int(raw_input("Enter speed 2 : "))
		s.append(v2)
		m+=1
	l.append(s)
	n+=1
print(l)
n=0
while n<a:
	k=l[n][1]+l[n][2]
	av=l[n][0]/k
	l.append(av)
	n+=1
print("List : ",l)