# Problem statement
# The lab built a homework bot. It does not give long speeches. It only answers one question: did this student pass the AI quiz?
# Write a function check_pass(marks) that returns True if marks >= 40, otherwise False. Do not print inside the function. Add a short docstring — even bots deserve documentation.
# Then read one quiz mark, call the function, and print Pass or Fail.
# Input
# One line: an integer marks (−100 ≤ marks ≤ 100).
# Output
# Print Pass or Fail.
# Examples
# Input
# 73
# Output
# Pass
# Input
# 39
# Output
# Fail

mrk=int(input())

def check_pass(marks):
    """
    Check pass or fail in the quiz test
    """
    if(marks>=40): return True
    else: return False

if(check_pass(mrk)):
    print("Pass")
else:
    print("Fail")


