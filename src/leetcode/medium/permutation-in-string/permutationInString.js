/*
https://leetcode.com/problems/permutation-in-string/description

You are given two strings s1 and s2.

Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

Both strings only contain lowercase letters.

Example 1:
Input: s1 = "abc", s2 = "lecabee"
Output: true
Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".

Example 2:
Input: s1 = "abc", s2 = "lecaabee"
Output: false

Constraints:
1 <= s1.length, s2.length <= 1000
*/

const checkInclusion = (s1, s2) => {
    const s1Chars = {};
    for (const char of s1) {
        s1Chars[char] = s1Chars[char] ?? 0;
        s1Chars[char] += 1;
    }

    let hasPermutation = false;
    let l = 0;
    let r = 0;

    while (r < s2.length) {
        const s2Char = s2[r];
        if (s1Chars[s2Char]) {
            s1Chars[s2Char] -= 1;

            if (s1Chars[s2Char] === 0) {
                delete s1Chars[s2Char];
            }

            if (Object.keys(s1Chars).length === 0) {
                hasPermutation = true;
                break;
            }

            r += 1;
        } else {
            const replacementS2Char = s2[l];
            s1Chars[replacementS2Char] = s1Chars[replacementS2Char] ?? 0;
            s1Chars[replacementS2Char] += 1;
            l += 1;
        }
    }

    return hasPermutation;
};

module.exports = { checkInclusion };
