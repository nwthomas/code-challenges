/*

https://leetcode.com/problems/group-anagrams/description/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

*/

function groupAnagrams(strs) {
    const tracker = {};

    for (let i = 0; i < strs.length; i++) {
        const keyMap = {};

        for (let c = 0; c < strs[i].length; c++) {
            const char = strs[i][c];
            keyMap[char] = keyMap[char] ? keyMap[char] + 1 : 1;
        }

        let keyString = "";
        for (const key of Object.keys(keyMap).sort()) {
            keyString += key.repeat(keyMap[key]);
        }

        tracker[keyString] = tracker[keyString]
            ? [...tracker[keyString], strs[i]]
            : [strs[i]];
    }

    return [...Object.values(tracker)];
}

module.exports = groupAnagrams;
