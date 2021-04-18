from __future__ import print_function
a=int(raw_input("Enter No. Of Data : "))
l=[]
n=0
while n<a:
	k=int(raw_input("Enter Value : "))
	l.append(k)
	n+=1
print(l)
n=0
s=[]
while n<a:
	t=0
	total=0
	count=0
	m=l[n]
	while m>0: #to count the no. of digits
		m/=10
		count+=1
	while l[n]>0:	# the main function
		t=(l[n]%10)*count
		total+=t
		l[n]/=10
		count-=1
	s.append(total)
	n+=1
print(s)

