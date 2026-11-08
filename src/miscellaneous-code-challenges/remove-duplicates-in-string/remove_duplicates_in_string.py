"""
You are given a string s and an integer k. Write a function to continuously remove all k adjacent duplicates from s, where the "adjacent" characters are equal, until none remain.

For instance, if k is 3 and the string is "daaabbbaa", since we have "aaa" and "bbb" as adjacent triples, the function should transform the string to "daa", removing the "aaa" substring and "bbb" substring.

Examples:
s = 'abcd'
k = 2
output: 'abcd'

s = 'deeedbbcccbdaa'
k = 3
output: 'aa'

s = 'pbbcggttciiippooaais'
k = 2
output: 'ps'

s = 'aaabbbacd'
k = 3
output: 'acd'

In each example, output refers to the resulting string after all possible k adjacent duplicates have been removed.
"""


def check_last_k_are_same(l: list[str], k: int) -> bool:
    last_k = l[len(l) - k:]
    last_k_set = set(last_k)

    return len(last_k_set) == 1


def identify_adjacent(s: str, k: int) -> str:
    stack = []

    for char in s:
        stack.append(char)

        if len(stack) >= k and check_last_k_are_same(stack, k):
            for _ in range(k):
                stack.pop()

    return "".join(stack)
