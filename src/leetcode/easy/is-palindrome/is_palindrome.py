"""
https://leetcode.com/problems/valid-palindrome/

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 
Constraints:
1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""

import re

PATTERN = r'[a-zA-Z0-9]'


def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        if not re.match(PATTERN, s[left]):
            left += 1
            continue
        if not re.match(PATTERN, s[right]):
            right -= 1
            continue

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True