/*

Good morning! Here's your coding interview problem for today.

This problem was asked by LinkedIn.

Given a string, return whether it represents a number. Here are the different kinds of numbers:
"10", a positive integer
"-10", a negative integer
"10.1", a positive real number
"-10.1", a negative real number
"1e5", a number in scientific notation

And here are examples of non-numbers:
"a"
"x 1"
"a -2"
"-"

*/

const isStringANumbers = numString => {
    if (typeof numString === "undefined" || numString.length <= 0) {
        return false;
    }
    const stringArray = numString.split("e");
    if (stringArray.length > 1) {
        let isNumber = true;
        for (const i in stringArray) {
            const converted = Number(stringArray[i]);
            if (Number.isNaN(converted) || stringArray[i].length <= 0) {
                isNumber = false;
            }
        }
        return isNumber;
    } else {
        let converted = Number(numString);
        return Number.isNaN(converted) ? false : true;
    }
};

module.exports = isStringANumbers;
