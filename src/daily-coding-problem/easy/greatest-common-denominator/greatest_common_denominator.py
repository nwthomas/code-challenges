"""

Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given n numbers, find the greatest common denominator between them.

For example, given the numbers [42, 56, 14], return 14.
"""


def find_greatest_common_denominator(num_list):
    lowest_cd = None
    isChanged = True
    current_try = 1

    while lowest_cd is None:
        for num in num_list:
            if num % current_try == 0:
                isChanged = True
                lowest_cd = current_try
            else:
                isChanged = False
                lowest_cd = None
                current_try += 1
                break
        if isChanged:
            break

    return lowest_cd
