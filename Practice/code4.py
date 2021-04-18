from __future__ import print_function
n=int(input("Enter Number Of Test Cases : "))
l=[]
for i in range(n): #Loop Of Test Cases
	data=input("Enter Data : ").split(" ")
	data=[int(x) for x in data]
	N,M,L=data[0],data[1],data[2]
	for j in range(N): #Loop for speed of bikers
		data1=input("Enter Speed : ").split(" ")
		data1=[int(y) for y in data1]
		l.extend(data1)
	k=1
	count=0
	while k<10:
		count+=1 
		l1=[]
		for t in (l[::2]):
			if (t>=L):
				l1.append(t)
		if (sum(l1)>=M): #sum of digits at even places
				break
		for s in (l[::2]):
			index1=l.index(s)
			l[index1]=l[index1]+l[index1+1]
		k+=1
print("Count : ",count-1)