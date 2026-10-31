
#  Given a list [1,2,3,4,5,6], use filter() to select even numbers and map() with lambda to square them.
# Sample Input:
#  No input
# Sample Output:
# [4, 16, 36]

lst=[1,2,3,4,5,6]

even=list(filter(lambda x: x%2==0,lst))
sq=list(map(lambda x:x*x,even))

print(sq)
