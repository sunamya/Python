from __future__ import print_function
a=int(raw_input("Enter No. Of Inputs : "))
l=[]
p=[]
n=0
while n<a:
	s=[]
	m=0
	tot=0
	while m<a:
		k=int(raw_input("Enter Value : "))
		s.append(k)
		tot+=k
		m+=1
	p.append(tot)
	l.append(s)
	n+=1
print(l)
print(p)
n=0
def sum(l):
	j=[]
	w=0
	while w<a:
		tot=0
		while l[w]>0:
			count=l[w]%10
			tot+=count
			l[w]/=10
		w+=1
		j.append(tot)
	print(j)
#print("List : ",l)
#print("Total : ",s)
sum(p)
