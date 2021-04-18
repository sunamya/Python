from __future__ import print_function
N,M,K=map(int,input().split())
A=input().split()
A=[int(x) for x in A]
U1=[]
U2=[]
U3=[]
index1=-1
index2=-1
if len(A)!=N:
	print("Error")
else:
	for i in range(M):
	    U=input().split()
	    U=[int(y) for y in U]
	    U1.append(U)
	    U2.extend(U)
	U2=set(U2)
	U2=list(U2)
	sum2=sum(U2)
	for a in range(N):
	    for b in range(N):
	        temp=[]
	        if (sum(U1[a])+sum(U1[b])==sum2):
	            temp=[i for w,q in zip(U1[a],U1[b]) if w==q]
	            if not temp:
	                index1=U1.index(U1[a])
	                index2=U1.index(U1[b])
	                U3.append(index1+1)
	                U3.append(index2+1)
	        break
for x in U2:
    if x in U3:
        U2.remove(x)
for x in U2:
    print(x,end=" ")