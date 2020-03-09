/*
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a start word, an end word, and a dictionary of valid words, find the shortest transformation
sequence from start to end such that only one letter is changed at each step of the sequence, and
each transformed word exists in the dictionary. If there is no possible transformation, return 
null. Each word in the dictionary have the same length as start and end and is lowercase.

For example, given start = "dog", end = "cat", and dictionary = {"dot", "dop", "dat", "cat"},
return ["dog", "dot", "dat", "cat"].

Given start = "dog", end = "cat", and dictionary = {"dot", "tod", "dat", "dar"}, return null as
there is no possible transformation from dog to cat.
*/

/**
 * Map over
 */

const findShortestTransformationSequence = (
    startString,
    endString,
    wordArray
) => {
    if (typeof startString !== "string") {
        throw new TypeError(
            "The first argument of findShortestTransformationSequence must be a string"
        );
    }
    if (typeof endString !== "string") {
        throw new TypeError(
            "The second argument of findShortestTransformationSequence must be a string"
        );
    }
    if (typeof wordArray !== "object") {
        throw new TypeError(
            "The third argument of findShortestTransformationSequence must be an object"
        );
    }
    const matchRecord = [startString];
    let currentWord = startString;
    for (let i = endString.length - 1; i >= 0; i--) {
        currentWord = startString.slice(0, i) + endString.slice(i);
        if (wordArray.indexOf(currentWord) >= 0 || currentWord === endString) {
            matchRecord.push(currentWord);
        } else {
            return null;
        }
    }
    return matchRecord;
};

module.exports = findShortestTransformationSequence;
