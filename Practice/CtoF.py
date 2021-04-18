from __future__ import print_function
def ctof(a):
	f=(a+32)*(9/5)
	return f
def ftoc(a):
	c=(a-32)*(5/9)
	return c
print("WELCOME\n1.FAHRANHEIT\n2.CELCIUS")
#c=int(raw_input("Enter Option : ")
t=float(raw_input("Enter Temperature : "))
c=int(raw_input("Enter Option : "))
if c==1:
	p=ftoc(t)
	print("Temperature : %1.5f",p)
elif c==2:
	p=ctof(t)
	print("Temperature : %1.5f",p)
else:
	print("Error")
