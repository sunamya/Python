from __future__ import print_function
def factorial(q):
    mul=1
    for t in range(1,q+1):
        mul*=t
    return mul
data=input().split(" ") #To Collect data
data=[int(x) for x in data] #Converting data into interger
n,k=data[0],data[1]
print(n,k)
l,l1=[],[]
r=factorial(2)
for i in range(1,n+1): #Calculating modulus
    remainder=i%k
    l.append(remainder)
print(l)
for j in range(k): #Pairing
    count=l.count(j)
    nr=count-r
    an=factorial(count)
    nr=factorial(nr)
    c1=int(an/(nr*r))
    if (c1==0):
        c1=1
    l1.append(c1)
print(sum(l1))