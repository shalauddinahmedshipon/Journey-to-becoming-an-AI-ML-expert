lst=input().split()
cntA=0
cntB=0
total=len(lst)
for i in range(total):
    if(lst[i]=='A'):
        cntA+=1
    else:
        cntB+=1

perA=(cntA/total)*100
perB=100-perA

if(perA>70 or perB>70):
    print("Biased Model")
else:
    print("Fair Model")