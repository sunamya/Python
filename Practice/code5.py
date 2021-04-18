from __future__ import print_function
T=int(input("Enter Number Of Test Cases : "))
for i in range(T):
	l=[]
	N=int(input("Enter Number Of elements in a list : "))
	data=input("Enter Data : ").split(" ")
	data=[int(x) for x in data]
	c=0
	for y in data:
		c=c|y
	print("Value is : ",c)
https://ide.geeksforgeeks.org/0dhcnKfgsp
https://ide.geeksforgeeks.org/1iGR8RtPd3