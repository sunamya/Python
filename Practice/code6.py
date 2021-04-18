from __future__ import print_function
T=int(input("Enter Number Of TestCases : "))
for i in range(T):
	l=[]
	N=int(input("Enter Size of the String : "))
	data=input("Enter Data : ").split(" ")
	for y in data:
		if y not in l:
			l.extend(y)
		else:
			l.append(-1)
	for x in l:
		print(x,end=" ")
https://ide.geeksforgeeks.org/TLMZezESXn