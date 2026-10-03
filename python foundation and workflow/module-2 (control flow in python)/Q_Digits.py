t=int(input())
for i in range(t):
    n=int(input())
    if(n==0):
        print(0)
        continue
    while n>0:
        print(n%10,end=" ")
        n//=10

    print()