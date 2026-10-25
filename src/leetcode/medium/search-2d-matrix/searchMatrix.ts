/*
https://leetcode.com/problems/search-a-2d-matrix/

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
*/

export function searchMatrix(matrix: number[][], target: number): boolean {
    if (matrix.length === 1 && matrix[0].length === 1) {
        return matrix[0][0] === target;
    }

    let left = 0;
    let right = matrix[0].length * matrix.length - 1;

    while (left < right) {
        const pivot = Math.floor((right + left) / 2);

        const pivotY = Math.floor(pivot / matrix[0].length);
        const pivotX = pivot % matrix[0].length;
        const currentNum = matrix[pivotY][pivotX];

        const leftY = Math.floor(left / matrix[0].length);
        const leftX = left % matrix[0].length;
        const leftNum = matrix[leftY][leftX];

        const rightY = Math.floor(right / matrix[0].length);
        const rightX = right % matrix[0].length;
        const rightNum = matrix[rightY][rightX];

        if (
            currentNum === target ||
            leftNum === target ||
            rightNum === target
        ) {
            return true;
        }

        if (currentNum < target) {
            left = pivot + 1;
        } else {
            right = pivot - 1;
        }
    }

    return false;
}
