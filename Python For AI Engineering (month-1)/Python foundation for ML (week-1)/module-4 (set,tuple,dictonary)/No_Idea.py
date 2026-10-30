lens=input().split()
n=int(lens[0])
m=int(lens[1])
lst=input().split()
lstA=input().split()
lstB=input().split()
setA=set()
setB=set()
for i in range(m):
    setA.add(int(lstA[i]))
    setB.add(int(lstB[i]))


happiness=0

for i in range(n):
    if(int(lst[i]) in setA):
        happiness+=1
    elif(int(lst[i]) in setB):
        happiness-=1


print(happiness)
