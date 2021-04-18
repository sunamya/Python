from __future__ import print_function
import random
q=[]
def display(x,l): #to display the chessboard
	n=0
	print(" ",end="")
	while n<x:
		print(chr(65+n),end="")
		n+=1
	n=0 
	print("\r")                 
	while n<x:
		m=0
		print(n+1,end="")
		while m<x:
			print(l[n][m],end="")
			m+=1
		print("\r")
		n+=1
def input(a,l,m): #to place the letter for chess
	if m=='K':
		m1='Q'
	else:
		m1='K'
	"""input from user"""
	yr=raw_input("Enter Rank : ").upper()
	yc=int(raw_input("Enter File : "))
	if (l[yc-1][ord(yr)-65])=='*':
		l[yc-1][ord(yr)-65]=m
	'''for generating random digits from computer'''
	cc=random.randrange(0,a,1)
	cr=chr(random.randrange(ord('A'),ord('A')+a,1))
	if (l[cc-1][ord(cr)-65])=='*':
		l[cc-1][ord(cr)-65]=m1
	c=check(yc-1,ord(yr)-65,cc-1,ord(cr)-65)
	check1(c)
	print(q)
	display(a,l)
def check(x,y,z,w):
	m=0
	c=0
	while x==z: #horizontal
		if m==w:
			c+=1
			break
		m+=1
	m=0
	while y==w: #vertical
		if x==z:
			c+=1
			break
		m+=1
	m=0 
	while (x+m<a) and (y+m<a) and (x-m>=0) and (y-m>=0): #forward diagonal
		if (x+m==z) and (y+m==w):
			c+=1
			break
		elif (x+m==z) and (y-m==w):
			c+=1
			break
		elif (x-m==z) and (y-m==w):
			c+=1
			break
		elif (x-m==z) and (y+m==w):
			c+=1
			break
		m+=1
	return c
def check1(c):
	if c>0:
		q.append('Y')
	else: 
		q.append('N')
"""main function starts"""
ch=int(raw_input("\nWELCOME TO CHESS!\n1. KING\n2. QUEEN\nEnter Your Choice : "))
a=int(raw_input("Enter test case : "))
l = [["*" for x in range(a)] for y in range(a)]
display(a,l)
n=0
while n<a:
	if ch==1:
		input(a,l,'K')
	elif ch==2:
		input(a,l,'Q')
	else:
		print("Wrong Choice!")
		break
	n+=1