# Take an integer N. Print all numbers from 1 to N, but skip multiples of 3 using continue. Sample Input: 10 Sample Output: 1 2 4 5 7 8 10

n = int(input())
for i in range(1,n+1):
    if(i%3==0):
        continue
    else:
        print(i,end=" ")