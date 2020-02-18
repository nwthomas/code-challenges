/*
Good morning! Here's your coding interview problem for today.

Given a 2-D matrix representing an image, a location of a pixel in the screen and a color C, replace the color of the given pixel and all adjacent same colored pixels with C.

For example, given the following matrix, and location pixel of (2, 2), and 'G' for green:

B B W
W W W
W W W
B B B
Becomes

B B G
G G G
G G G
B B B
*/

function replacePixels(arr, point, newColor) {
    if (!Array.isArray(arr) || !arr.length) {
        throw new TypeError("The 2D matrix must be an array with sub-arrays");
    }
    if (
        !Array.isArray(point) ||
        typeof point[0] !== "number" ||
        typeof point[1] !== "number"
    ) {
        throw new TypeError("The point must be an array of two numbers");
    }
    if (point.length < 2 || point.length > 2) {
        throw new TypeError("The point must exactly contain an X and Y axis");
    }
    if (
        newColor.length > 1 ||
        newColor.length < 1 ||
        typeof newColor !== "string"
    ) {
        throw new TypeError(
            "The new color must be a string with one character"
        );
    }
    if (!arr.length) {
        return arr;
    }
    const replacedColor = arr[point[0]][point[1]];
    const tracker = new Set();
    let newArr = [...arr];
    function replace(_point = point) {
        if (tracker.has(_point)) {
            return;
        } else {
            if (newArr[_point[0]][_point[1]] === replacedColor) {
                newArr[_point[0]][_point[1]] = newColor;
            }
            tracker.add(_point);
            if (_point[0] - 1 > 0) {
                replace([_point[0] - 1, _point[1]]);
            }
            if (_point[1] - 1 > 0) {
                replace([_point[0], _point[1] - 1]);
            }
            if (_point[0] + 1 < arr.length) {
                replace([_point[0] + 1, _point[1]]);
            }
            if (_point[1] + 1 < arr[_point[0]].length) {
                replace([_point[0], _point[1] + 1]);
            }
        }
    }
    replace();
    return newArr;
}

function deepCopy(arr = []) {
    if (!Array.isArray(arr)) {
        throw new TypeError("The argument of deepCopy must be an array");
    }
    const copiedArr = [];
    arr.forEach(value => {
        if (Array.isArray(value)) {
            copiedArr.push(deepCopy(value));
        } else {
            copiedArr.push(value);
        }
    });
    return copiedArr;
}

module.exports = { replacePixels, deepCopy };
