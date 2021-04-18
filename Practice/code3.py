from __future__ import print_function
n=int(input("Enter Number of Test Cases : "))
for i in range(n): #Loop for test Cases
	count=0
	no=int(input("Enter Number Of Strings : "))
	strings=input("Enter String : ")
	strings=strings.split(" ")
	strings="".join(strings)
	l=len(strings)
	l1=int(l/2)
	j=1
	while (j<l1):
		if (strings[l1-j]!=strings[l1+j]):
			strings=strings[:((l1-j))]+strings[((l1-j)+1):]
			print(strings)
			count+=1
			l2=len(strings)
			l1=int(l2/2)
		else:
			j+=1
	print(count)