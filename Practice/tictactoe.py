from __future__ import print_function
import random
def display1(l):
	n=0
	while n<3:
		m=0
		print("-------------")
		print("| ",end="")
		while m<3:
			print(l[n][m],end=" | ")
			m+=1
		print("\r")
		n+=1
	print("-------------")
def play(x,l):
	d=0
	e=0
	if x=='X':
		x1='O'
	else:
		x1='X'
	a=int(raw_input("Enter Position(1-9) : "))
	c=random.randrange(2,9,1)
	print(c)
	if a!=c:
		if a in range(1,4):
			if (l[0][a-1])=="":
				l[0][a-1]=x
				d=check(l,x)
		elif a in range(4,7):
			if (l[1][a-4])=="":
				l[1][a-4]=x
				d=check(l,x)
		elif a in range(7,10):
			if (l[2][a-7])=="":	
				l[2][a-7]=x
				d=check(l,x)
		else:
			print("WRONG VALUE!")
		if c in range(1,4):
			if (l[0][c-1])=="":
				l[0][c-1]=x1
				e=check(l,x1)
		elif c in range(4,7):
			if (l[1][c-4])=="":
				l[1][c-4]=x1
				e=check(l,x1)
		elif c in range(7,10):
			if (l[2][c-7])=="":
				l[2][c-7]=x1
				e=check(l,x1)
		else:
			print("WRONG VALUE!")
	display1(l)
	return (d,e)
def check(l,x):
	c=0
	if ((l[0][0] == x and l[0][1] == x and l[0][2] == x) or (l[1][0] == x and l[1][1] == x and l[1][2] == x) or (l[2][0] == x and l[2][1] == x and l[2][2] == x) or (l[0][0] == x and l[1][0] == x and l[2][0] == x) or (l[0][1] == x and l[1][1] == x and l[2][1] == x) or (l[0][2] == x and l[1][2] == x and l[2][2] == x) or (l[0][0] == x and l[1][1] == x and l[2][2] == x) or (l[0][2] == x and l[1][1] == x and l[2][0] == x)):
		c=1
	print(c)
	return c
"""main function starts here"""
l = [["" for x in range(3)] for y in range(3)]
ch=int(raw_input("WELCOME TO TIC TAC TOE WORLD\n1. X\n2. O\nCHOOSE YOUR SYMBOL : "))
c1=0
c2=0
n=0
while n<4 and c1==0 and c2==0:
	if ch==1:
		print("YOU ARE : X AND COMPUTER IS : O")
		c1,c2=play('X',l)
	elif ch==2:
		print("YOU ARE : O AND COMPUTER IS : X")
		c1,c2=play('O',l)
	else:
		print("WRONG CHOICE!")
		break
	if c1>0 or c2>0:
		break
	n+=1
if c1>0:
	print("YOU WIN!")
elif c2>0:
	print("COMPUTER WIN!")
else:
	print("DRAW!")