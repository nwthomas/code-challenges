"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Dropbox.

What does the below code snippet print out? How can we fix the anonymous functions to behave 
as we'd expect?

functions = []
for i in range(10):
    functions.append(lambda : i)

for f in functions:
    print(f())
"""


def print_ten_lambdas():
    functions = []
    num = 0

    def create_lambda(num):
        def l(): return num
        return l

    while (num <= 9):
        functions.append(create_lambda(num))
        num += 1

    return functions
