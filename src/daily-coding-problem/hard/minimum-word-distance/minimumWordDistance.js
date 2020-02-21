/*
Good morning! Here's your coding interview problem for today.

Find an efficient algorithm to find the smallest distance (measured in number of words)
between any two given words in a string.

For example, given words "hello", and "world" and a text content of "dog cat hello cat
dog dog hello cat world", return 1 because there's only one word "cat" in between the two words.
*/

const findMinimumWordDistance = (wordOne, wordTwo, wordString) => {
    if (typeof wordOne !== "string") {
        throw new TypeError("The first argument must be a string");
    }
    if (typeof wordTwo !== "string") {
        throw new TypeError("The second argument must be a string");
    }
    if (typeof wordString !== "string") {
        throw new TypeError("The third argument must be a string");
    }
    if (wordString.length < wordOne.length + wordTwo.length + 1) {
        throw new TypeError(
            "The length of the third argument must be greater than the length of the first two arguments"
        );
    }
    const wordStringArray = wordString.split(" ");
    let isTracking = false;
    let foundDistance = 0;
    let tracker = 0;
    wordStringArray.forEach(word => {
        if (word === wordOne && isTracking) {
            tracker = 0;
        } else if (word === wordTwo && isTracking) {
            if (foundDistance === 0 || foundDistance > tracker) {
                foundDistance = tracker;
            }
        } else if (word === wordOne && !isTracking) {
            isTracking = true;
        } else {
            tracker++;
        }
    });
    return foundDistance;
};

module.exports = findMinimumWordDistance;
