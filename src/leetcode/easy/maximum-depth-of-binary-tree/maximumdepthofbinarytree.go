/*
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Constraints:
The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
*/

package maximumdepthofbinarytree

type TreeNode struct {
	Val int
	Left *TreeNode
	Right *TreeNode
}

type Tracker struct {
    Depth int
    Node  *TreeNode
}

func maxDepth(root *TreeNode) int {
    maxDepth := 0
    tracker := []Tracker{}
    if root != nil {
        tracker = append(tracker, Tracker{
            Depth: 1,
            Node: root,
        })
    }

    for len(tracker) > 0 {
        current := tracker[len(tracker)-1]
        tracker = tracker[:len(tracker)-1]
        if current.Depth > maxDepth {
            maxDepth = current.Depth
        }
        if current.Node.Left != nil {
            tracker = append(tracker, Tracker{
                Depth: current.Depth + 1,
                Node: current.Node.Left,
            })
        }
        if current.Node.Right != nil {
            tracker = append(tracker, Tracker{
                Depth: current.Depth + 1,
                Node: current.Node.Right,
            })
        }
    }

    return maxDepth
}