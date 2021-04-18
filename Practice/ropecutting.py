from __future__ import print_function
def ropecut(r): #Function starts here
	l=[]
	while (len(r)>0):
		minimum=min(r)
		count=r.count(minimum)
		r=[int(y-minimum) for y in r]
		for w in range(count):
			r.remove(0)
		count1=len(r)
		if (count1>0):
			l.append(count1)
	for q in l:
		print(q,end=" ")
n=int(input("Enter Test Cases : ")) #Main Function starts here
for i in range(n):
	rope=int(input("Enter No. Of Rope : "))
	x=input("Enter Length : ")
	if len(x)==(2*rope-1):
		r=x.split(" ")
		r=[int(y) for y in r]
		ropecut(r)
	else:
		print("Size Mismatch")