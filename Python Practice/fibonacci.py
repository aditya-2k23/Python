"""
Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones.
In this module, we calculate and print the first 10 numbers in the Fibonacci sequence.
"""

A = 0
B = 1
for i in range(10):
    print(A, end=" ")
    A, B = (B, A + B)

    # * This is a tuple assignment
    # ? In tuple assignment, the right-hand side of the assignment is evaluated first.
    # ? Then the items on the right-hand side are assigned to the items on the left-hand side.
    # ?(Value of B is assigned to A)
    # ? (And the value of A + B is assigned to B)
