/*
https://leetcode.com/problems/same-tree/

Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure
and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.
*/

package sametree

type TreeNode struct {
	Val int
	Left *TreeNode
	Right *TreeNode
}

type Tracker struct {
    P  *TreeNode
    Q *TreeNode
}

func isSameTree(p *TreeNode, q *TreeNode) bool {
    if p != nil && q == nil || p == nil && q != nil {
        return false
    }

    tracker := []Tracker{}
    if p != nil && q != nil {
        tracker = append(tracker, Tracker{
            P: p,
            Q: q,
        })
    }

    for len(tracker) > 0 {
        current := tracker[len(tracker)-1]
        tracker = tracker[:len(tracker)-1]

        nextLeftP := current.P.Left
        nextLeftQ := current.Q.Left
        nextRightP := current.P.Right
        nextRightQ := current.Q.Right

        if current.P.Val != current.Q.Val {
            return false
        }
        if nextLeftP != nil && nextLeftQ == nil || nextLeftP == nil && nextLeftQ != nil {
            return false
        }
        if nextRightP != nil && nextRightQ == nil || nextRightP == nil && nextRightQ != nil {
            return false
        }

        if nextLeftP != nil {
            tracker = append(tracker, Tracker{
                P: nextLeftP,
                Q: nextLeftQ,
            })
        }
        if nextRightP != nil {
            tracker = append(tracker, Tracker{
                P: nextRightP,
                Q: nextRightQ,
            })
        }
    }

    return true
}