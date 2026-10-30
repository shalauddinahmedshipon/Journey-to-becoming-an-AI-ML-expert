# use py2 version
n=int(raw_input())
inp=raw_input().split()
nums=list()
for i in range(n):
    nums.append(int(inp[i]))

t=tuple(nums)
print(hash(t))
