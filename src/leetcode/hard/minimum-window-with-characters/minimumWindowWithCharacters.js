/*
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
*/

function minWindow(s, t) {
    if (t.length > s.length || t === "") {
        return "";
    }

    let tracker = {};
    for (const char of t) {
        tracker[char] = tracker[char] || 0;
        tracker[char] += 1;
    }

    const window = {};
    let have = 0;
    let need = Object.keys(tracker).length;
    let l = 0;
    let res = "";
    let resLen = Infinity;

    for (let r = 0; r < s.length; r++) {
        const char = s[r]
        window[char] = window[char] || 0;
        window[char] += 1;

        if (window[char] === tracker[char]) {
            have += 1;
        }

        while (have === need) {
            if ((r - l + 1) < resLen) {
                resLen = r - l + 1;
                res = s.substring(l, r + 1);
            }

            window[s[l]] -= 1;
            if (tracker[s[l]] && window[s[l]] < tracker[s[l]]) {
                have -= 1;
            }
            l += 1;
        }
    }

    return res;
}

module.exports = { minWindow };