package binarysearch

import (
	"testing"
)

func TestBinarySearch(t *testing.T) {
	tests := []struct {
		name string
		nums []int
		target int
		want int
	}{
		{name: "test 1", nums: []int{1,2,3,4,5,6,7,8,9,10}, target: 5, want: 4},
		{name: "test 2", nums: []int{1,2,3,4,5,6,7,8,9,10}, target: 1, want: 0},
		{name: "test 3", nums: []int{1,2,3,4,5,6,7,8,9,10}, target: 10, want: 9},
		{name: "test 4", nums: []int{1,2,3,4,5,6,7,8,9,10}, target: 11, want: -1},
	}
	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			got := binarySearch(test.nums, test.target)
			if got != test.want {
				t.Errorf("binarySearch(%v, %d) = %d, want %d", test.nums, test.target, got, test.want)
			}
		})
	}
}