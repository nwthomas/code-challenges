/*
Write a function that accepts two square matrices (N x N two dimensional arrays), and return the sum of the two. Both matrices being passed into the function will be of size N x N (square), containing only integers.

How to sum two matrices:

Take each cell [n][m] from the first matrix, and add it with the same [n][m] cell from the second matrix. This will be cell [n][m] of the solution matrix.

Visualization:
|1 2 3|     |2 2 1|     |1+2 2+2 3+1|     |3 4 4|
|3 2 1|  +  |3 2 3|  =  |3+3 2+2 1+3|  =  |6 4 4|
|1 1 1|     |1 1 3|     |1+1 1+1 1+3|     |2 2 4|

Example:
matrixAddition(
  [ [1, 2, 3],
    [3, 2, 1],
    [1, 1, 1] ],
    
    +

  [ [2, 2, 1],
    [3, 2, 3],
    [1, 1, 3] ] )

returns:
  [ [3, 4, 4],
    [6, 4, 4],
    [2, 2, 4] ]
*/

function matrixAddition(a, b) {
    if (!Array.isArray(a) || !Array.isArray(b)) {
        throw new TypeError(
            "Both arguments in matrixAddition must be of type Array"
        );
    }

    if (
        !a.length ||
        a.filter((val) => !val.length).length ||
        !b.length ||
        b.filter((val) => !val.length).length
    ) {
        return [];
    }

    const solution = deepCopy(a);

    b.forEach((arr, arrIndex) => {
        arr.forEach((num, numIndex) => {
            solution[arrIndex][numIndex] += num;
        });
    });

    return solution;
}

function deepCopy(arr) {
    const finalArr = [];

    arr.forEach((val) => {
        if (Array.isArray(val)) {
            finalArr.push(deepCopy(val));
        } else {
            finalArr.push(val);
        }
    });

    return finalArr;
}

module.exports = matrixAddition;
