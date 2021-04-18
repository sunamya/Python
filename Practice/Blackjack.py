from __future__ import print_function
a=int(raw_input("Enter No. of Testcases : "))
n=0
t=[]
while n<a:
	ch='Y'
	l=[]
	while ch=='Y':
		d=raw_input("Choice : ").upper()
		l.append(d)
		ch=raw_input("Want to enter more? : ").upper()
	m=0
	s=0
	while m<len(l):
		if s>21:
			s="burst"
			break
		if (l[m]=='J' or l[m]=='Q' or l[m]=='K' or l[m]=='T'):
			s+=10
		elif (ord(l[m])>=50 and ord(l[m])<=57):
			s+=(ord(l[m])-48)
		if l[m]=='A':
			if (s+11)>21:
				s+=1
			else:
				s+=11
		m+=1
	t.append(s)
	n+=1
print(t)