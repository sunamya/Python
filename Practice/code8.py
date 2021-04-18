from __future__ import print_function
N=int(input()) #Total Number Of Tickets
data=[]
for i in range(N):
	temp=input() #Enter The Ticket ID
	data.append(temp)
count=0
for x in data:
	index=data.index(x)
	for y in data[index:]:
		if x!=y:
			c=1
			s=x+y
			s=[int(d) for d in s]
			for z in range(0,10):
				if z not in s:
					c=0
					break
			if c==1:
				count+=1
print(count)