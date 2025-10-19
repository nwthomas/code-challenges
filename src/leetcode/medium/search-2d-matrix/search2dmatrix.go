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
