package search2dmatrix

import (
	"testing"
)

func TestSearch2DMatrix(t *testing.T) {
	tests := []struct {
		name string
		matrix [][]int
		target int
		want bool
	}{
		{name: "test 1", matrix: [][]int{{1,3,5,7},{10,11,16,20},{23,30,34,60}}, target: 3, want: true},
		{name: "test 2", matrix: [][]int{{1,3,5,7},{10,11,16,20},{23,30,34,60}}, target: 13, want: false},
		{name: "test 3", matrix: [][]int{{1}}, target: 1, want: true},
		{name: "test 4", matrix: [][]int{{1}}, target: 2, want: false},
		{name: "test 5", matrix: [][]int{{1,3},{5,7}}, target: 3, want: true},
		{name: "test 6", matrix: [][]int{{1,3},{5,7}}, target: 5, want: true},
	}
	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			got := searchMatrix(test.matrix, test.target)
			if got != test.want {
				t.Errorf("searchMatrix(%v, %d) = %t, want %t", test.matrix, test.target, got, test.want)
			}
		})
	}
}