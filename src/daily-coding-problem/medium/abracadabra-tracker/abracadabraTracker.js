/*
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Given a string and a pattern, find the starting indices of all occurrences of the pattern in the string. For example, given the string "abracadabra" and the pattern "abr", you should return [0, 7].
*/

const findPatternStartingIndices = (pattern, string) => {
    const indicesArray = [];
    const patternLength = pattern.length;

    for (let i = 0; i < string.length; i++) {
        const stringSlice = string.slice(i, i + patternLength);

        if (stringSlice === pattern) {
            indicesArray.push(i);
        }

        if (i + patternLength > string.length) {
            break;
        }
    }

    return indicesArray;
};

module.exports = findPatternStartingIndices;
