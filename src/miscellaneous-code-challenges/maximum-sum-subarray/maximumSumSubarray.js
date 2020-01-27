/*
This solution uses Kadane's Algorithm for the classic maximum subarray problem.

In this algorithm, you should do the following:
1. Track a running total for the array of numbers
2. Track the maximum total found so far
3. If the total + next number are greater than the maximum total so far, total equals maximum number
4. If the total becomes negative, reset total to 0
5. Return the maximum total when finished iterating through the array of numbers
*/

const findMaxSumSubarray = numberArray => {
    let maxTotal = null;
    let currentTotal = 0;
    numberArray.forEach(num => {
        currentTotal += num;
        if (!maxTotal || currentTotal > maxTotal) {
            maxTotal = currentTotal;
        }
        if (currentTotal < 0) {
            currentTotal = 0;
        }
    });
    return maxTotal;
};

module.exports = findMaxSumSubarray;
