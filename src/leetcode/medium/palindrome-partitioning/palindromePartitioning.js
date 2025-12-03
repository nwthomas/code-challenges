/*
https://leetcode.com/problems/palindrome-partitioning

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]
 
Constraints:
1 <= s.length <= 16
s contains only lowercase English letters.
*/

const palindromePartitioning = (s) => {
    const result = [];
    const part = [];

    function isPalindrome(s, l, r) {
        while (l < r) {
            if (s[l] !== s[r]) {
                return false;
            }
            l += 1;
            r -= 1;
        }

        return true;
    }

    function backtrack(i) {
        if (i >= s.length) {
            result.push([...part]);
            return;
        }

        for (let j = i; j < s.length; j++) {
            if (isPalindrome(s, i, j)) {
                part.push(s.substring(i, j + 1));
                backtrack(j + 1);
                part.pop();
            }
        }
    }

    backtrack(0);

    return result;
};

module.exports = { palindromePartitioning };
