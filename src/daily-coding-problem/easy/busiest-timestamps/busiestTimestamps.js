/*
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

You are given a list of data entries that represent entries and exits of groups of people into a building. An entry looks like this:

{"timestamp": 1526579928, count: 3, "type": "enter"}

This means 3 people entered the building. An exit looks like this:

{"timestamp": 1526580382, count: 2, "type": "exit"}

This means that 2 people exited the building. timestamp is in Unix time.

Find the busiest period in the building, that is, the time with the most people in the building. Return it as a pair of (start, end) timestamps. You can assume the building always starts off and ends up empty, i.e. with 0 people inside.
*/

function findBusiestTime(dataObjectArray) {
    /**
     * Takes in an array of data objects and then sorts for the time period where
     * the building was the busiest
     *
     * @param {array} dataObjectArray An array of data objects in the format of
     * {"timestamp": 1526580382, count: 2, "type": "exit"}
     *
     * @returns {array} A tuple of the beginning and ending timestamp when the
     * building was the busiest.
     */
    let finalTimestamps = [];
    let largestTotal = 0;
    let total = 0;
    dataObjectArray.forEach(dataObject => {
        dataObject.type === "enter"
            ? (total += dataObject.count)
            : (total -= dataObject.count);
        if (total > largestTotal) {
            largestTotal = total;
            finalTimestamps = [dataObject.timestamp];
        } else if (finalTimestamps.length && total < largestTotal) {
            finalTimestamps.push(dataObject.timestamp);
        }
    });
    return finalTimestamps;
}

module.exports = findBusiestTime;
