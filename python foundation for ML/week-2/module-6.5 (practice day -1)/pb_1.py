# Problem 1
# Write a function introduce(name, age) that prints:

# My name is <name> and I am <age> years old.
 
# Call it using positional arguments.

# Sample Input:
# Rahim 28
# Sample Output:
# My name is Rahim and I am 28 years old.

inp=input().split()
name=inp[0]
age=inp[1]

def introduce(name,age):
    print(f"My name is {name} and I am {age} years old.")

introduce(name,age)



