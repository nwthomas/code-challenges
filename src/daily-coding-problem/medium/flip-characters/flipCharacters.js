/*
Good morning! Here's your coding interview problem for today.

This problem was asked by LinkedIn.

You are given a string consisting of the letters x and y, such as xyxxxyxyy. In addition, you have an operation called flip, which changes a single x to y or vice versa.

Determine how many times you would need to apply this operation to ensure that all x's come before all y's. In the preceding example, it suffices to flip the second and sixth characters, so you should return 2.
*/

function flipChars(str, c1, c2) {
    if (
        typeof str !== "string" ||
        typeof c1 !== "string" ||
        typeof c2 !== "string"
    ) {
        throw new TypeError(
            "All three arguements for flipChars must be of type string."
        );
    }

    if (!str.length || !c1.length || !c2.length) {
        return 0;
    }

    const strArr = str.split("");
    let left = 0;
    let right = str.length - 1;
    let count = 0;

    while (left < right) {
        if (strArr[left] === c1 || strArr[right] === c2) {
            strArr[left] === c1 && left++;
            strArr[right] === c2 && right--;
        } else {
            [strArr[left], strArr[right]] = [strArr[right]];
            strArr[left] = c1;
            strArr[right] = c2;
            count += 2;
        }
    }

    return count;
}

module.exports = flipChars;
