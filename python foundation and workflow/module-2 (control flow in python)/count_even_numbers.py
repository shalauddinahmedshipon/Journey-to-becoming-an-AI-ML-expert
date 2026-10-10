n=int(input())
inp=input()
numbers=inp.split()
ans=0
for i in range(n):
    if(int(numbers[i])%2==0):
        ans+=1

print(ans)