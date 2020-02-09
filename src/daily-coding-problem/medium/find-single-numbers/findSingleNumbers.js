/*
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given an array of integers in which two elements appear exactly once and all other elements appear exactly twice, find the two elements that appear only once.

For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8. The order does not matter.

Follow-up: Can you do this in linear time and constant space?
*/

function findSingleNumbers(arr) {
    /**
     * Finds the two instances of unique numbers in an array of numbers
     *
     * @param {array} arr An array of integer numbers
     *
     * @returns {array} Returns an array with two unique instances of numbers or else an
     * empty array.
     */

    const tracker = {};
    const singleNumsTotal = [];
    if (arr.length < 2 || !Array.isArray(arr)) {
        return singleNumsTotal;
    }
    arr.forEach(num => {
        tracker[num] ? tracker[num]++ : (tracker[num] = 1);
    });
    const totals = Object.entries(tracker);
    totals.forEach(total => {
        if (total[1] === 1) {
            singleNumsTotal.push(Number(total[0]));
        }
    });
    if (singleNumsTotal.length === 2) {
        return singleNumsTotal;
    } else {
        return [];
    }
}

module.exports = findSingleNumbers;
