from __future__ import print_function
T=int(input()) #Enter the no. of test cases
i,s=0,0
l=["chef","chfe","cehf","cefh","cfeh","cfhe","ecfh","echf","efch","efhc","ehcf","ehfc","fceh","fche","fech","fehc","fhec","fhce","hcfe","hcef","hecf","hefc","hfec","hfce"]
len1=len(l)
while (i<T):
	S=input() #Enter the string
	length=len(S)
	s+=length
	count=0
	if (s<2,000,000 and length<500,000):
		if (length<=2000):
			for j in range(len1):
				if l[j] in S:
					count+=1
	if (count>0):
		print("lovely"," ",count)
	else:
		print("Normal")
	i+=1