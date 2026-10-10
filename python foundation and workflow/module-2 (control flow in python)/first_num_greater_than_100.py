n=int(input())
inp=input()
nums=inp.split()
isDetected=False
ans=0
for i in range(n):
    x=int(nums[i])
    if(x>100 and isDetected==False):
        ans=x
        isDetected=True
        break
    elif(x<=100):
        continue

if(isDetected==False):
    print("Not Found")
else:
    print(x)
        