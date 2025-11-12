"""
https://leetcode.com/problems/longest-repeating-character-replacement/

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 
Constraints:
1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
"""

def characterReplacement(s: str, k: int) -> int:
    cache = {}
    longest = 0
    l, r = 0, 0
    maxFrequent = 0

    while r < len(s):
        cache[s[r]] = cache.get(s[r], 0) + 1
        maxFrequent = max(maxFrequent, cache[s[r]])

        while (r - l + 1) - maxFrequent > k:
            cache[s[l]] -= 1
            l += 1

        longest = max(longest, r - l + 1)
        r += 1
            
    return longest