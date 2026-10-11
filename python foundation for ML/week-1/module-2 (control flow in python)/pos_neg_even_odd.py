n=int(input())
inp=input()
numbers=inp.split()

pos=0 ;neg=0 ;even=0 ;odd=0

for i in range(n):
    x=int(numbers[i])
    if(x%2==0):
        even+=1
    else:
        odd+=1

    if(x>0):
        pos+=1
    elif(x<0):
        neg+=1

print("Positive:",pos)
print("Negative:",neg)
print("Even:",even)
print("Odd:",odd)
        
