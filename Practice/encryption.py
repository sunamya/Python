from __future__ import print_function
a=int(raw_input("Enter How Many Lines : "))
b=int(raw_input("Number of encryption : "))	
n=0
while n<a:
	t=raw_input("Enter Data(encypted) : ").upper()
	s=list(t)
	m=0
	while m<len(t):
		if ord(t[m])==32:
			s[m]=t[m]
		elif (ord(t[m])-b)<65:
			s[m]=90-(65-(ord(t[m])-b))+1
			s[m]=chr(s[m])
		else:
			s[m]=ord(t[m])-b
			s[m]=chr(s[m])
		m+=1
	s="".join(s)
	print(s)
	n+=1
