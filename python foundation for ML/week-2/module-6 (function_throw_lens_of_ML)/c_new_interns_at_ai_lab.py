# Problem statement
# Two new interns just walked in. Security will not open the GPU room without an ID card. Your job is the card printer.
# Write student_card(name, roll, dept) that prints:
# <name> | Roll: <roll> | Dept: <dept>
# You will get two interns. Call the function twice with positional arguments: name, then roll, then dept. Swap the order and someone from EEE will get into the CSE GPU queue. Chaos.
# Input
# Two lines. Each line: name roll dept (name and dept are one word).
# Output
# Two ID lines, same order as input.
# Example
# Input
# Rafi 101 CSE
# Mim 102 EEE
# Output
# Rafi | Roll: 101 | Dept: CSE
# Mim | Roll: 102 | Dept: EEE



def student_card(name, roll, dept):
    print(f"{name} | Roll: {roll} | Dept: {dept}")

user1=input().split()
name1=user1[0]
roll1=user1[1]
dep1=user1[2]

user2=input().split()
name2=user2[0]
roll2=user2[1]
dep2=user2[2]

student_card(name1,roll1,dep1)
student_card(name2,roll2,dep2)