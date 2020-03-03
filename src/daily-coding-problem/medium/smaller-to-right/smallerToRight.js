/*
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given an array of integers, return a new array where each element in the new array is the number of smaller elements to the right of that element in the original input array.

For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:

There is 1 smaller element to the right of 3
There is 1 smaller element to the right of 4
There are 2 smaller elements to the right of 9
There is 1 smaller element to the right of 6
There are no smaller elements to the right of 1
*/

function findSmallerToTheRightInArray(arrayOfNumbers) {
    /**
     * Takes in an array of numbers and returns an array of numbers where each one is the sum of
     * the number of integers to its right in the array that are less than it.
     *
     * @param {array} arrayOfNumbers The input array of numbers
     *
     * @returns {array} The returned array of numbers
     */
    if (!Array.isArray(arrayOfNumbers)) {
        throw new TypeError("The argument must be an array");
    }
    if (!arrayOfNumbers.length) {
        return [];
    }
    const tracker = {};
    const final = [];
    arrayOfNumbers.reverse().forEach(num => {
        if (typeof num !== "number") {
            throw new TypeError("The array must only contain numbers");
        }
        let numberSmaller = 0;
        for (let trackedNum in tracker) {
            trackedNum < num && (numberSmaller += tracker[trackedNum]);
        }
        tracker[num] ? (tracker[num] += 1) : (tracker[num] = 1);
        final.push(numberSmaller);
    });
    return final.reverse();
}

module.exports = findSmallerToTheRightInArray;
