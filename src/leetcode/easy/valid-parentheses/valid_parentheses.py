"""
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

def get_is_valid_parentheses(s: str) -> bool:
    inputsMap = {
        ")": "(",
        "}": "{",
        "]": "[",
    }
    tracker = []
    
    for char in s:
        if len(tracker) > 0 and char in inputsMap and tracker[len(tracker) - 1] == inputsMap[char]:
            tracker.pop()
        else:
            tracker.append(char)
            
    return len(tracker) == 0