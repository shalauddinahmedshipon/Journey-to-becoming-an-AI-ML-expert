# Problem 2

# Write a Python generator function called batch_generator. It should take a list of numbers (representing data samples) and a batch_size. The generator should yield one batch at a time as a list.

# Example Input:
# data = [1, 2, 3, 4, 5, 6, 7, 8]
# batch_size = 3

# Expected Output (when iterated):
# [1, 2, 3]
# [4, 5, 6]
# [7, 8]

lst=list(map(int,input().split()))
b_sz=int(input())

def generate_batch(data,batch_size):
    for i in range(0,len(data),batch_size):
        yield data[i:i+batch_size]

batch=generate_batch(lst,b_sz)
i=len(lst)
while(i>0):
    print(next(batch))
    i-=b_sz

