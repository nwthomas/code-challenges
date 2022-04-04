"""
Given a box of chocolate bars of dimension N x M, choose an area a x a such that for all a, 1 <= a <= min(N, M). Given multiple values of N and M, find the number of ways to choose the area of dimension a x a from the box of dimension N x M for all a.

For example, given a box of bars where N = 2 and M = 2, there is one way to have a 2 x 2 bar, and there are 4 ways to choose a 1 x 1 bar. In this case, the number of ways to choose a x a bars for all valid values of a is 5.

FUNCTION DESCRIPTION
complete the function numberOfWays below. The function must return an list of long integers where element i denotes the result of the inputted cases.

numberOfWays has the following parameter(s):
1. cases[cases[0],....cases[n-1]]: a 2D array of integers with dimensions as number of cases x 2

CONSTRAINTS
1. 1 <= number of test cases <= 2500
2. 1 <= N, M <= 2500

SAMPLE INPUT FOR TESTING
[[3, 4], [6, 5]] 
Should output [20, 70]

EXPLANATION OF SAMPLE INPUT
There are t = 2 test cases
In the 1st test case, N = 3 and M = 4
The number of ways to select an area of dimensions 1 is 12, of dimension 2 is 6, and of dimension 3 is 2.
"""


def numberOfWays(cases):
    total = [0 for i in range(len(cases))]
    for i in range(len(cases)):
        least = min(cases[i][0], cases[i][1])
        most = max(cases[i][0], cases[i][1])
        for j in range(0, least * most):
            if j + 1 > least:
                break
            else:
                total[i] += (most - j) * (least - j)
    return total
