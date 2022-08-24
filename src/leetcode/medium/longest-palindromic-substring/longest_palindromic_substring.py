"""
https://leetcode.com/problems/longest-palindromic-substring

Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
"""

def longest_palindrome(s: str) -> str:
    longest = ""
    
    for i in range(len(s)):
        l = i
        r = i + 1
        current = ""
        
        while l >= 0 and r < len(s) and s[l] == s[r]:
            current = s[l:r + 1]
            l -= 1
            r += 1
            
        longest = current if len(current) > len(longest) else longest
        current = s[i]
        
        l = i - 1
        r = i + 1
        
        while l >= 0 and r < len(s) and s[l] == s[r]:
            current = s[l:r + 1]
            l -= 1
            r += 1
            
        longest = current if len(current) > len(longest) else longest
    
    return longest