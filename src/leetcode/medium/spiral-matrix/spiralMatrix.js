/*
https://leetcode.com/problems/spiral-matrix/

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
*/

const RIGHT = "right";
const DOWN = "down";
const LEFT = "left";
const UP = "up";

const spiralOrder = (matrix) => {
    const result = [];
    // Can be: "right", "down", "left", "up"
    let direction = RIGHT;
    let offset = 0;
    let x = 0;
    let y = 0;

    while (true) {
        result.push(matrix[y][x]);

        if (direction == RIGHT) {
            if (x < matrix[0].length - 1 - offset) {
                x += 1;
            } else {
                direction = DOWN;
                y += 1;
            }
        } else if (direction === DOWN) {
            if (y < matrix.length - 1 - offset) {
                y += 1;
            } else {
                direction = LEFT;
                x -= 1;
            }
        } else if (direction === LEFT) {
            if (x > 0 + offset) {
                x -= 1;
            } else {
                direction = UP;
                offset += 1;
                y -= 1;
            }
        } else {
            if (y > 0 + offset) {
                y -= 1;
            } else {
                direction = RIGHT;
                x += 1;
            }
        }

        if (result.length === matrix.length * matrix[0].length) {
            break;
        }
    }

    return result;
};

module.exports = { spiralOrder };
