from __future__ import print_function
a=int(raw_input("Enter Data Length : "))
n=0
l=[]
while n<a:
	k=raw_input("Enter : ")
	l.append(k)
	n+=1
print("List : ",l)
n=0
while n<a:
	count=0
	b=0
	x=len(l[n])
	while b<x:
		if ((l[n][b].upper()=='A') or (l[n][b].upper()=='E') or (l[n][b].upper()=='I') or (l[n][b].upper()=='O') or (l[n][b].upper()=='U')):
			count+=1
		b+=1
	print(x)
	print("Vowel : ",count)
	n+=1