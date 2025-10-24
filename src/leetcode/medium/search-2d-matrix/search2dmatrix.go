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

package search2dmatrix

func searchMatrix(matrix [][]int, target int) bool {
    rows, cols := len(matrix), len(matrix[0])
    l, r := 0, rows * cols -1

    for l <= r {
        m := l + (r - l) / 2
		// row = m divided by columns to get y, col = m modulo by colums to get x
        row, col := m / cols, m % cols
		lRow, lCol := l / cols, l % cols
		rRow, rCol := r / cols, r % cols

		// Perform three checks (l, m, r) every time to speed up the search
        if matrix[row][col] == target || matrix[lRow][lCol] == target || matrix[rRow][rCol] == target {
            return true
        } else if matrix[row][col] < target {
            l = m + 1
        } else {
            r = m - 1
        }
    }

    return false
}
