package maximumdepthofbinarytree

import (
	"testing"
)

func TestMaxDepth(t *testing.T) {
	tests := []struct {
		name string
		root *TreeNode
		want int
	}{
		{name: "huge tree", root: &TreeNode{Val: 1, Right: &TreeNode{Val: 2, Right: &TreeNode{Val: 3, Right: &TreeNode{Val: 4, Right: &TreeNode{Val: 5, Right: &TreeNode{Val: 6, Right: &TreeNode{Val: 7, Right: &TreeNode{Val: 8, Right: &TreeNode{Val: 9, Right: &TreeNode{Val: 10}}}}}}}}}}, want: 10},
		{name: "medium tree", root: &TreeNode{Val: 3, Left: &TreeNode{Val: 9}, Right: &TreeNode{Val: 20, Left: &TreeNode{Val: 15}, Right: &TreeNode{Val: 7}}}, want: 3},
		{name: "short tree", root: &TreeNode{Val: 1, Right: &TreeNode{Val: 2}}, want: 2},
		{name: "root is nil", root: nil, want: 0},
	}
	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			got := maxDepth(test.root)
			if got != test.want {
				t.Errorf("maxDepth(%v) = %d, want %d", test.root, got, test.want)
			}
		})
	}
}