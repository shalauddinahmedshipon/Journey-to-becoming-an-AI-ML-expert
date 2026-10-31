n=int(input())
inp=input()
numbers=inp.split()
even=0 ;odd=0 ;pos=0 ;neg=0

for i in range(n):
    x=int(numbers[i])
    if x>0:
        pos+=1
    elif x<0:
        neg+=1

    if x%2==0:
        even+=1
    else:
        odd+=1

print("Even:",even)
print("Odd:",odd)
print("Positive:",pos)
print("Negative:",neg)
