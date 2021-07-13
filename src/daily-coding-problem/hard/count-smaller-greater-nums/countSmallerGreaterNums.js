/*
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Let A be an N by M matrix in which every row and every column is sorted.

Given i1, j1, i2, and j2, compute the number of elements of M smaller than M[i1, j1] and larger than M[i2, j2].

For example, given the following matrix:

[[1, 3, 7, 10, 15, 20],
 [2, 6, 9, 14, 22, 25],
 [3, 8, 10, 15, 25, 30],
 [10, 11, 12, 23, 30, 35],
 [20, 25, 30, 35, 40, 45]]
And i1 = 1, j1 = 1, i2 = 3, j2 = 3, return 15 as there are 15 numbers in the matrix smaller than 6 or greater than 23.
*/

function countSmallerGreaterNums(matrix, i1, j1, i2, j2) {
    let total = 0;

    if (
        [i1, j1, i2, j2].filter((arg) => typeof arg !== "number").length > 0 ||
        !matrix.length ||
        !matrix[0].length
    ) {
        return total;
    }

    const smaller = matrix[i1][j1];
    const larger = matrix[i2][j2];

    if (typeof smaller !== "number" || typeof larger !== "number") {
        return total;
    }

    let y = 0;
    let x1 = 0;
    let x2 = matrix[0].length;

    while (y < matrix.length) {
        x2 = matrix[y].length;
        const currentRow = matrix[y];

        if (currentRow[x1] > larger || currentRow[x2] < smaller) {
            total += currentRow.length;
        } else {
            while (x1 < x2) {
                if (currentRow[x1] < smaller) {
                    total += 1;
                }

                if (currentRow[x2] > larger) {
                    total += 1;
                }

                x1 += 1;
                x2 -= 1;
            }
        }

        x1 = 0;
        y += 1;
    }

    return total;
}

module.exports = countSmallerGreaterNums;
