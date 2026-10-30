# Keep taking integers as input. Add them to a total. Stop when a negative number appears (break). Do not add that negative number. Then print the total. Sample Input: 4 8 15 -3 23 Sample Output: 27

inp=input()
nums=inp.split()
size=len(nums)
sum=0
for i in range(size):
    x=int(nums[i])
    if(x<0):
        break
    else:
        sum+=x

print(sum)
