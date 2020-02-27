/*
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given a string, determine whether any permutation of it is a palindrome.

For example, carrace should return true, since it can be rearranged to form racecar, which is a palindrome. daily should return false, since there's no rearrangement that can form a palindrome.
*/

function isPermutationPalindromePossible(wordString) {
    if (typeof wordString !== "string") {
        throw new TypeError(
            "The argument for isPermutationPalindromePossible must be a string"
        );
    }

    const tracker = wordString.split("").reduce((accum, char) => {
        const newAccum = accum;
        newAccum[char] ? newAccum[char]++ : (newAccum[char] = 1);
        return newAccum;
    }, {});

    let oddLetter = null;
    const keys = Object.keys(tracker);

    for (let i = 0; i < keys.length; i++) {
        if (tracker[keys[i]] >= 2) {
            tracker[keys[i]] -= 2;
            tracker[keys[i]] >= 1 && i--;
        } else if (!oddLetter) {
            tracker[keys[i]] -= 1;
            oddLetter = true;
        } else if (oddLetter && tracker[keys[i]] === 1) {
            return false;
        } else {
            return true;
        }
        tracker[keys[i]] === 0 && delete tracker[keys[i]];
    }

    return Object.keys(tracker).length ? false : true;
}

module.exports = isPermutationPalindromePossible;
