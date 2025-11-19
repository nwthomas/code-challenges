/*
https://leetcode.com/problems/generate-parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
 

Constraints:
1 <= n <= 8
*/

const generateParenthesis = (n) => {
    function backtrack(str, open, closed) {
        if (open === 1 && closed === n - 1) {
            return [str + ")"];
        }

        const result = [];
        if (open > 0) {
            result.push(...backtrack(str + ")", open - 1, closed + 1));
        }
        if (open < n && closed < n) {
            result.push(...backtrack(str + "(", open + 1, closed));
        }

        return result;
    }

    return backtrack("(", 1, 0);
}

module.exports = { generateParenthesis };