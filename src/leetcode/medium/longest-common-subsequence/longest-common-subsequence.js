/*
https://leetcode.com/problems/longest-common-subsequence/

Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

Constraints:
1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.

*/

function getLongestCommonSubsequence(text1, text2) {
    const grid = [];
    for (let y = 0; y <= text1.length; y++) {
        const row = [];

        for (let x = 0; x <= text2.length; x++) {
            row.push(0);
        }

        grid.push(row);
    }

    for (let y = text1.length - 1; y >= 0; y--) {
        for (let x = text2.length - 1; x >= 0; x--) {
            if (text1[y] === text2[x]) {
                grid[y][x] = 1 + grid[y + 1][x + 1];
            } else {
                grid[y][x] = Math.max(grid[y + 1][x], grid[y][x + 1]);
            }
        }
    }

    return grid[0][0];
}

module.exports = getLongestCommonSubsequence;
