# F. GPU Can Eat Only Three Images (Hard)
# Problem statement
# TinyNet is hungry. You have a list of training samples (think: face images for age-group classification). The lab GPU is small. It can swallow only batch_size samples at a time.
# Write a generator batch_generator(data, batch_size) that yields one batch (a list) at a time — like giving the GPU one plate, not the whole buffet. The last plate may have fewer samples. If batch_size < 1, the GPU is off: yield nothing.
# Also write batch_mean(batch) that returns the average of the numbers in that batch. The senior uses this as a tiny sanity check before real training.
# Read the samples and the batch size. For each batch print:
# [1, 2, 3] mean=2.0
# Input
# First line: two integers n and batch_size (n ≥ 1).
# Second line: n integers — the sample values.
# Output
# One line per batch: the batch list, a space, then mean= and the mean.
# If batch_size < 1, print nothing.
# Example
# Input
# 8 3
# 1 2 3 4 5 6 7 8
# Output
# [1, 2, 3] mean=2.0
# [4, 5, 6] mean=5.0
# [7, 8] mean=7.5

inp=list(map(int,input().split()))
n=inp[0]
b_sz=inp[1]
lst=list(map(int,input().split()))

def batch_generator(data,chunk_size):
    for i in range(0,n,chunk_size):
        yield data[i:i+chunk_size]

def batch_mean(batch):
    sum=0
    for i in range(len(batch)):
        sum+=batch[i]
    avg=sum/len(batch)
    return avg
         

x=batch_generator(lst,b_sz)
i=n
while(i>0):
    i-=b_sz
    new_list=next(x)
    mean=batch_mean(new_list)
    print(new_list,f"mean={mean}")



