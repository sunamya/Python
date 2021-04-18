from __future__ import print_function
n=int(input("Enter Number Of Test Cases : "))
no=int(input("Enter Number OF Houses : "))
for i in range(1,no):
	road=input().split(" ") #Fetching data in single line
	road=[int(x) for x in road] #Converting into integer
print(road)
