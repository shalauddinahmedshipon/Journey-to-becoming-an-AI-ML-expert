n=int(input())
t=float(input())
total_loss=0
i=n
while(i>0):
    x=float(input())
    total_loss+=x
    i-=1


avg_loss=(total_loss/n)

if(avg_loss<=t):
    print("PASS")
else:
    print("RETRY")
