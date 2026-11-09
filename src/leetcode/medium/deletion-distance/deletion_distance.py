"""
https://leetcode.com/problems/delete-operation-for-two-strings

Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.

Example 1:
Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Example 2:
Input: word1 = "leetcode", word2 = "etco"
Output: 4
 
Constraints:
1 <= word1.length, word2.length <= 500
word1 and word2 consist of only lowercase English letters.
"""


def deletion_distance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)

    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i

    for i in range(n + 1):
        dp[0][i] = i

    for y in range(1, m + 1):
        char1 = word1[y - 1]

        for x in range(1, n + 1):
            char2 = word2[x - 1]

            if char2 == char1:
                dp[y][x] = dp[y - 1][x - 1]
            else:
                dp[y][x] = min(
                    dp[y - 1][x] + 1,
                    dp[y][x - 1] + 1,
                )

    return dp[-1][-1]
