"""
https://leetcode.com/problems/partition-labels

You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

Example 1:
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]

Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

Example 2:
Input: s = "eccbbbbdec"
Output: [10]

Constraints:
1 <= s.length <= 500
s consists of lowercase English letters.
"""


def partitionLabels(s: str) -> list[int]:
    tracker = {}

    for i, char in enumerate(s):
        tracker[char] = i

    res = []
    size, end = 0, 0
    for i, char in enumerate(s):
        size += 1
        end = max(end, tracker[char])

        if i == end:
            res.append(size)
            size = 0

    return res
