"""
https://leetcode.com/problems/multiply-strings

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"

Constraints:
1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""


def multiply(num1: str, num2: str) -> str:
    res = "0"

    if "0" in [num1, num2]:
        return "0"

    for i, num in enumerate(num1[::-1]):
        curr = multiplyOneNum(num, num2, i)
        res = add(res, curr)

    return res


def multiplyOneNum(num: str, num2: str, placeValue: int) -> str:
    res = ""
    num2 = num2[::-1]
    carriedNum = 0

    for i in range(len(num2)):
        curr = int(num) * int(num2[i])
        curr += carriedNum
        carriedNum = 0

        while curr >= 10:
            curr -= 10
            carriedNum += 1

        res += f"{curr}"

    if carriedNum > 0:
        res += f"{carriedNum}"

    res = res[::-1]

    while placeValue > 0:
        res += "0"
        placeValue -= 1

    return res


def add(num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0":
        return num2 if num1 == "0" else num1

    res = ""
    i = 0
    num1 = num1[::-1]
    num2 = num2[::-1]
    carry = False

    while i < len(num1) or i < len(num2):
        curr = 0
        if carry:
            curr += 1
            carry = False

        if i > len(num1) - 1:
            curr += int(num2[i])
        elif i > len(num2) - 1:
            curr += int(num1[i])
        else:
            curr += int(num1[i]) + int(num2[i])

        if curr >= 10:
            curr -= 10
            carry = True

        i += 1
        res += f"{curr}"

    if carry:
        res += "1"

    return res[::-1]
