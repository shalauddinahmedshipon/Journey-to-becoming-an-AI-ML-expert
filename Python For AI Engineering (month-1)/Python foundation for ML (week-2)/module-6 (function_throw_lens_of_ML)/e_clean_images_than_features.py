# E. Clean Images, Then Features (Medium)
# Problem statement
# You have a folder of face-image IDs for an age-detection toy model. Odd IDs are blurry selfies. Even IDs are clean.
# Keep only the clean (even) IDs, then turn each one into a dummy feature by squaring it. Yes, squaring an ID is a silly feature. The senior said: “First learn filter and map. Fancy embeddings can wait.”
# You must use filter() + lambda to keep evens, then map() + lambda to square. Print the final list of features.
# Input
# First line: integer n (1 ≤ n ≤ 100) — how many IDs.
# Second line: n integers — the image IDs.
# Output
# Print a Python list of squared even IDs, same order. Example: [4, 16, 36].
# Example
# Input
# 6
# 1 2 3 4 5 6
# Output
# [4, 16, 36]

n=int(input())
lst=map(int,input().split())

new_lst=list(filter(lambda x:x%2==0,lst))
result=list(map(lambda x:x*x,new_lst))

print(result)
