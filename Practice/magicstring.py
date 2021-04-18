from __future__ import print_function
def convert(s): #Function
	l=list(s)
	length=len(s)
	if (l[0]>='A' and l[0]<='Z'):
		for i in range(length):
			if (i%2==0):
				l[i]=l[i].upper()
			else:
				l[i]=l[i].lower()
	else:
		for i in range(length):
			if (i%2==0):
				l[i]=l[i].lower()
			else:
				l[i]=l[i].upper()
	s="".join(l)
	print("String is :",s)
n=int(input("Enter Number Of Test Cases : ")) #Main Function
for x in range(n):
	s=input("Enter String : ")
	convert(s)