from __future__ import print_function
import random
a=int(raw_input("Enter No. Of Matches : "))
n=0
while n<a:
	print("ROUND ",n+1)
	c1=0
	c2=0
	while c1<5 and c2<5:
		c=random.choice(["P","R","S"])
		u=raw_input("Enter Character : ").upper()
		print(u)
		print("Computer : ",c)
		if u!='P' and u!='R' and u!='S':
			print("Wrong Value entered")
			c1+=1
			continue
		if c=='P' and u=='R':
			c1+=1
		elif c=='P' and u=='S':
			c2+=1
		elif c=='R' and u=='P':
			c2+=1
		elif c=='R' and u=='S':
			c1+=1
		elif c=='S' and u=='P':
			c1+=1
		elif c=='S' and u=='R':
			c2+=1
		else:
			continue
	print("ROUND ",n+1, "SCORE : Computer : ",c1," Human : ",c2)
	if c1>c2:
		print("Computer Wins!")
	elif c1<c2:
		print("You Win!")
	else:
		print("DRAW")
	n+=1
