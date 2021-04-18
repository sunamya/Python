from __future__ import print_function
a=int(raw_input("Enter no. of try : "))
b=int(raw_input("Enter Secret Value : "))
n=0
l=[]
l1=[]
while n<a:
	t=int(raw_input("Enter Guess : "))
	s=b
	c=0
	t2=[]
	s2=[]
	while t>0 and s>0: #checking the exact position
		s1=s%10
		t1=t%10
		s/=10
		t/=10
		t2.append(t1)
		s2.append(s1)
		if s1==t1:
			c+=1
	l.append(c)
	m=0
	c1=0
	while m<len(t2): #checking numbers
		w=0
		while w<len(s2):
			if t2[m]==s2[w]:
				c1+=1
			w+=1
		m+=1
	l1.append(c1)
	n+=1
n=0
while n<len(l) and n<len(l1):
	print(l[n],"-",l1[n])
	n+=1