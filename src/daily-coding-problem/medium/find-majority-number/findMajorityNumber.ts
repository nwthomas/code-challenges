/*
Good morning! Here's your coding interview problem for today.

This problem was asked by MongoDB.

Given a list of elements, find the majority element which appears more than half the time.

You can assume that such element exists.

For example, given [1, 2, 1, 1, 1, 3, 4, 0], return 1.
*/

const getArrayLength = (arr: number[]) => Math.ceil(arr.length / 2);

const trackNewNumber = (num: number, tracker: Record<number, number>) => {
    const newTracker = { ...tracker };
    if (num in tracker) {
        newTracker[num]++;
    } else {
        newTracker[num] = 1;
    }
    return newTracker;
};

const checkForHalfNumber = (
    num: number,
    tracker: Record<number, number>,
    halfLength: number,
) => {
    if (tracker[num] >= halfLength) {
        return true;
    } else {
        return false;
    }
};

const findMoreThanHalfNumber = (arr: number[]) => {
    if (!Array.isArray(arr)) {
        throw new TypeError(
            "You must pass an array of numbers into findMoreThanHalfNumber",
        );
    }
    let tracker: Record<number, number> = {};
    let foundNumber = null;
    const halfArrayLength = getArrayLength(arr);
    for (let i = 0; i < arr.length; i++) {
        tracker = trackNewNumber(arr[i], tracker);
        if (checkForHalfNumber(arr[i], tracker, halfArrayLength)) {
            foundNumber = arr[i];
            break;
        }
    }
    return foundNumber;
};

export {
    getArrayLength,
    trackNewNumber,
    checkForHalfNumber,
    findMoreThanHalfNumber,
};
