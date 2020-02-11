/*
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given an array of numbers and an index i, return the index of the nearest larger number of the number at index i, where distance is measured in array indices.

For example, given [4, 1, 3, 5, 6] and index 0, you should return 3.

If two distances to larger numbers are the equal, then return any one of them. If the array at i doesn't have a nearest larger integer, then return null.

Follow-up: If you can preprocess the array, can you do this in constant time?
*/

function findNearestLargerNumber(numberArray = [], index = null) {
    /**
     * Takes in a number array with an index and returns the index of the nearest larger integer
     * in either direction of the array.
     *
     * @param {array} numberArray The number array used to find the next largest integer. It
     * defaults to an empty array.
     *
     * @param {number} index The index of the number to be compared when searching for the next largest integer.
     *
     * @returns {number} The integer of the next larger integer in the numberArray.
     */

    if (!Array.isArray(numberArray)) {
        throw new TypeError(
            "The first argument for findNearestLargerNumber must be an array of numbers"
        );
    }

    if (typeof index !== "number") {
        throw new TypeError(
            "The second argument for findNearestLargerNumber must be a number"
        );
    }

    let rightIndex = index > 0 ? index - 1 : index;
    let leftIndex = index < numberArray.length - 1 ? index + 1 : index;
    let isRightFound = false;
    let isLeftFound = false;
    let running = true;

    while (running) {
        if (numberArray[rightIndex] > numberArray[index]) {
            isRightFound = true;
            running = false;
        }
        if (numberArray[leftIndex] > numberArray[index]) {
            isLeftFound = true;
            running = false;
        }
        running && rightIndex > 0 && rightIndex--;
        running && leftIndex < numberArray.length - 1 && leftIndex++;
    }

    if (!isRightFound && !isLeftFound) {
        return null;
    } else if (isRightFound && isLeftFound) {
        return rightIndex;
    } else if (isRightFound) {
        return rightIndex;
    } else if (isLeftFound) {
        return leftIndex;
    } else {
        return null;
    }
}

module.exports = findNearestLargerNumber;
