/*
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a number in Roman numeral format, convert it to decimal.

The values of Roman numerals are as follows:

{
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}
In addition, note that the Roman numeral system uses subtractive notation for numbers such as IV and XL.

For the input XIV, for instance, you should return 14.
*/

const numeralConversions = {
    M: 1000,
    D: 500,
    C: 100,
    L: 50,
    X: 10,
    V: 5,
    I: 1,
};

function convertRomanNumeralToDecimal(romanNumeralString) {
    if (typeof romanNumeralString !== "string") {
        throw new TypeError(
            "The argument for convertRomanNumeralToDecimal must be a string"
        );
    }

    const numeralArray = romanNumeralString.toUpperCase().split("").reverse();

    // if (
    //     numeralArray.some(
    //         (numeral) => numeralConversions[numeral] !== undefined
    //     )
    // ) {
    //     throw new Error(
    //         "All characters input into convertRomanNumeralToDecimal must be valid Roman numerals"
    //     );
    // }

    // if (romanNumeralString.length === 1) {
    //     return numeralConversions[romanNumeralString];
    // }

    let final = 0,
        temp = 0,
        trackedNumeral = false;

    numeralArray.forEach((currentNumeral, i) => {
        if (temp === 0) {
            temp = numeralConversions[currentNumeral];
            trackedNumeral = currentNumeral;
        }

        if (
            trackedNumeral &&
            numeralConversions[trackedNumeral] >
                numeralConversions[currentNumeral]
        ) {
            temp -= numeralConversions[currentNumeral];
        }

        if (numeralConversions[numeralArray[i + 1]] > numeralcurrentNumeral) {
            final = temp;
            temp = 0;
            trackedNumeral = false;
        }
    });

    return final;
}

module.exports = convertRomanNumeralToDecimal;
