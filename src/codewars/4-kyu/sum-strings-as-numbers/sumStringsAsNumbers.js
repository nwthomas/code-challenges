/*
Given the string representations of two integers, return the string representation of the sum of those integers.

For example:

sumStrings('1','2') // => '3'
A string representation of an integer will contain no characters besides the ten numerals "0" to "9".
*/

function sumStrings(a, b) {
    const aNums = a.split("").reverse();
    const bNums = b.split("").reverse();
    const total = [];

    let carryOver = 0;

    for (let i = 0; i < Math.max(aNums.length, bNums.length); i++) {
        let tempTotal = carryOver;
        carryOver = 0;
        if (aNums[i]) {
            tempTotal += parseFloat(aNums[i]);
        }
        if (bNums[i]) {
            tempTotal += parseFloat(bNums[i]);
        }
        if (tempTotal >= 10) {
            carryOver = 1;
            tempTotal -= 10;
        }
        total.push(tempTotal);
    }

    if (carryOver) {
        total.push(carryOver);
    }

    while (total[total.length - 1] === 0) {
        total.pop();
    }

    return total.reverse().join("");
}

module.exports = sumStrings;
