package sametree

import (
	"testing"
)

func TestIsSameTree(t *testing.T) {
	tests := []struct {
		name string
		root1 *TreeNode
		root2 *TreeNode
		want bool
	} {
		{name: "test 1", root1: &TreeNode{Val: 1, Left: &TreeNode{Val: 2}, Right: &TreeNode{Val: 3}}, root2: &TreeNode{Val: 1, Left: &TreeNode{Val: 2}, Right: &TreeNode{Val: 3}}, want: true},
		{name: "test 2", root1: &TreeNode{Val: 1, Left: &TreeNode{Val: 2}, Right: &TreeNode{Val: 3}}, root2: &TreeNode{Val: 1, Left: &TreeNode{Val: 2}, Right: &TreeNode{Val: 4}}, want: false},
		{name: "test 3", root1: nil, root2: &TreeNode{Val: 1, Left: &TreeNode{Val: 2}, Right: &TreeNode{Val: 3}}, want: false},
		{name: "test 4", root1: &TreeNode{Val: 1, Left: &TreeNode{Val: 2}, Right: &TreeNode{Val: 3}}, root2: nil, want: false},
		{name: "test 5", root1: nil, root2: nil, want: true},
	}
	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			got := isSameTree(test.root1, test.root2)
			if got != test.want {
				t.Errorf("isSameTree(%v, %v) = %v, want %v", test.root1, test.root2, got, test.want)
			}
		})
	}
}