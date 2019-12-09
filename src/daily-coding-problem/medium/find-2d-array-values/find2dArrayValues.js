/*

Good morning! Here's your coding interview problem for today.

This problem was asked by Apple.

Suppose you have a multiplication table that is N by N. That is, a 2D array where the value at the i-th row and j-th column is (i + 1) * (j + 1) (if 0-indexed) or i * j (if 1-indexed).

Given integers N and X, write a function that returns the number of times X appears as a value in an N by N multiplication table.

For example, given N = 6 and X = 12, you should return 4, since the multiplication table looks like this:

| 1 | 2 | 3 | 4 | 5 | 6 |

| 2 | 4 | 6 | 8 | 10 | 12 |

| 3 | 6 | 9 | 12 | 15 | 18 |

| 4 | 8 | 12 | 16 | 20 | 24 |

| 5 | 10 | 15 | 20 | 25 | 30 |

| 6 | 12 | 18 | 24 | 30 | 36 |

And there are 4 12's in the table.

*/

function createArray(x, y) {
  if (typeof x !== "number" || typeof y !== "number") {
    return null;
  }
  const array = Array(y).fill([]);
  for (let xIndex = 0; xIndex < array.length; xIndex++) {
    let tempArray = Array(x).fill(null);
    tempArray = tempArray.map((_, yIndex) => {
      return (xIndex + 1) * (yIndex + 1);
    });
    array[xIndex] = tempArray;
  }
  return array;
}

function flattenArray(array) {
  if (!array.length || typeof array !== "object") {
    return null;
  }
  if (array.length <= 0) {
    return array;
  }
  let final = [];
  for (let i = 0; i < array.length; i++) {
    if (typeof array[i] === "object" && array[i].length) {
      final = final.concat(flattenArray(array[i]));
    } else {
      final.push(array[i]);
    }
  }
  return final;
}

function findValues(x, y, value) {
  if (
    typeof x !== "number" ||
    typeof y !== "number" ||
    typeof value !== "number"
  ) {
    return null;
  }
  const array = createArray(x, y);
  const flattened = flattenArray(array);
  const final = flattened.reduce((accum, current) => {
    if (current === value) {
      return (accum = accum + 1);
    } else {
      return accum;
    }
  }, 0);
  return final;
}

module.exports = {
  createArray,
  findValues,
  flattenArray
};
