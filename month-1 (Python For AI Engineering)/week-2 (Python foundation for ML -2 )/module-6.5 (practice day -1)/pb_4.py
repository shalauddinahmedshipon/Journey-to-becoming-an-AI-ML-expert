#  Write a function power(base, exponent) that returns the result of base raised to exponent. If the exponent is not given, it should calculate the square.
# Sample Input:
# 5
# Sample Output:
# 25
# Sample Input 2:
# 5 3
# Sample Output 2:
# 125

inp=list(map(int,input().split()))
n=inp[0]
if(len(inp)==2):
    exp=inp[1]
else:
    exp=2

def power(base,exp):
    res=base
    for i in range(1,exp):
     res*=base

    return res

ans=power(n,exp)
print(ans)