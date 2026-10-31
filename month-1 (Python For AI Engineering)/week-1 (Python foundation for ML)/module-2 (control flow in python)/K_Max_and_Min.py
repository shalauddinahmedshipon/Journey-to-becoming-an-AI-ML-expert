inp=input()
numbers=inp.split()
a=int(numbers[0])
b=int(numbers[1])
c=int(numbers[2])

mn=a
mx=a

if b<mn:
    mn=b
if c<mn:
    mn=c

if b>mx:
    mx=b
if c>mx:
    mx=c

print(mn,mx)