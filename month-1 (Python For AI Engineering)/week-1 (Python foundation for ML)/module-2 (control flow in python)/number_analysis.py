n=int(input())
inp=input()
numbers=inp.split()
cnt=0

for i in range(n):
    x=int(numbers[i])
    if(x%2==0):
        continue
    else:
        sum=0
        n=x
        while(n>0):
            sum+=n%10
            n//=10
            if(sum>=20):
                break

        if(sum>=20):
            break
        else:
            print(x,sum)
            cnt+=1

print(cnt)