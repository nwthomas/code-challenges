"""
https://leetcode.com/problems/minimum-window-substring/

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Constraints:
m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.

Follow up: Could you find an algorithm that runs in O(m + n) time?
"""


def minWindow(s: str, t: str) -> str:
    if len(t) > len(s) or t == "":
        return ""

    c = {}
    for char in t:
        if not char in c:
            c[char] = 0
        c[char] += 1

    tracker = {}
    have = 0
    need = len(list(c.keys()))
    l = 0
    res = ""
    resLen = float("inf")
    for r, char in enumerate(s):
        if not char in tracker:
            tracker[char] = 0
        tracker[char] += 1

        if char in c and tracker[char] == c[char]:
            have += 1

        while have == need:
            if r - l + 1 < resLen:
                resLen = r - l + 1
                res = s[l : r + 1]

            tracker[s[l]] -= 1
            if s[l] in c and tracker[s[l]] < c[s[l]]:
                have -= 1
            l += 1

    return res
