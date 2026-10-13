n=int(input())
cntYes=0
cntNo=0
i=n
while(i>0):
    vote=input()
    if(vote=="YES"):
        cntYes+=1
    else:
        cntNo+=1
    i-=1

if(cntYes>=cntNo):
    print("ACCEPT")
else:
    print("REJECT")