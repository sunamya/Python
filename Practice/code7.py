from __future__ import print_function
N=int(input())
l=[]
names=[] #Total Number Of Participants
for i in range(N):
	data=input().split(" ")
	data1=[int(x) for x in data[1:]]
	del data[1:]
	names.extend(data)
	data.extend(data1)
	match=data[2]-data[1]
	l.append(match)
maximum=max(l)
index=l.index(maximum)
name=names[index]
print(name,maximum)