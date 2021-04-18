from __future__ import print_function
def staircase(n):
    # Complete this function
    for i in range(n):
        for j in range(n):
            if ((i+j)>=n-1):
                print("#",end='')
            else:
                print(" ",end='')

if __name__ == "__main__":
    n = int(input().strip())
    staircase(n)