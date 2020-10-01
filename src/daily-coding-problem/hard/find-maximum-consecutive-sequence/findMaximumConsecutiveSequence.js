/*
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a list of integers L, find the maximum length of a sequence of consecutive numbers that can be formed using elements from L.

For example, given L = [5, 2, 99, 3, 4, 1, 100], return 5 as we can build a sequence [1, 2, 3, 4, 5] which has length 5.
*/

const findMaximumConsecutiveSequence = (numberArray) => {
    const sortedNumberArray = quickSort(numberArray);
    let longestSequence = 0;
    let currentSequence = 0;

    sortedNumberArray.forEach((num, i) => {
        if (!longestSequence) {
            currentSequence += 1;
            longestSequence = currentSequence;
        } else if (num - 1 === sortedNumberArray[i - 1]) {
            currentSequence += 1;
            if (currentSequence > longestSequence) {
                longestSequence = currentSequence;
            }
        } else {
            currentSequence = 1;
        }
    });

    return longestSequence;
};

const quickSort = (numberArray) => {
    if (numberArray.length <= 1) {
        return numberArray;
    }

    const guess = numberArray[Math.floor(Math.random() * numberArray.length)];

    const lower = numberArray.filter((num) => num < guess);
    const equal = numberArray.filter((num) => num === guess);
    const higher = numberArray.filter((num) => num > guess);

    return quickSort(lower).concat(equal.concat(quickSort(higher)));
};

module.exports = findMaximumConsecutiveSequence;
