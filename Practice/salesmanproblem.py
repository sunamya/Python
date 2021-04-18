from __future__ import print_function
import numpy as np
def salesman(r,size): #Function
	for a in range(size):
		for b in range(size):
			print(min(r[a]))
n=int(input("Enter Number Of Test Cases : ")) #Main Function
for z in range(n):
	size=int(input("Enter Size of the array : "))
	x=input("Enter Cost : ")
	r=x.split(" ")
	r=[int(y) for y in r]
	#Conversioin of a list(array) into 2D matrix
	r=np.array(r)
	shape=(size,size)
	r=np.matrix(r.reshape(shape))
	salesman(r,size)