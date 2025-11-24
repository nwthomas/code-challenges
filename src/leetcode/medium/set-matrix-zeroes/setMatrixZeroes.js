/*
https://leetcode.com/problems/set-matrix-zeroes

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
*/

const setMatrixZeroes = (matrix) => {
    const rows = {};
    const columns = {};

    for (let y = 0; y < matrix.length; y++) {
        for (let x = 0; x < matrix[y].length; x++) {
            if (matrix[y][x] === 0) {
                rows[y] = true;
                columns[x] = true;
            }
        }
    }

    for (const y of Object.keys(rows)) {
        for (let x = 0; x < matrix[y].length; x++) {
            matrix[y][x] = 0;
        }
    }

    for (const x of Object.keys(columns)) {
        for (let y = 0; y < matrix.length; y++) {
            matrix[y][x] = 0;
        }
    }

    return matrix;
};

module.exports = { setMatrixZeroes };
