import sys
n=int(input())
inp=input()
numbers=inp.split()
mn=sys.maxsize
mx=0
for i in range(n):
    x=int(numbers[i])
    if(x<mn):
        mn=x

    if(x>mx):
        mx=x

print(mn,mx)
