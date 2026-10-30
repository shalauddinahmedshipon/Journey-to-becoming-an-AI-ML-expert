# Take an integer N. Use a for loop and range to print all odd numbers from 1 to N. Sample Input: 10 Sample Output: 1 3 5 7 9

n=int(input())
for i in range(1,n+1,2):
    print(i,end=" ")