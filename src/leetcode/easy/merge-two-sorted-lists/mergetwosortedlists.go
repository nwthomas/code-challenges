package mergetwosortedlists

type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
    dummy := &ListNode{}
    node := dummy

    for list1 != nil && list2 != nil {
        if list1.Val < list2.Val {
            node.Next = list1
            list1 = list1.Next
        } else {
            node.Next = list2
            list2 = list2.Next
        }
        node = node.Next
    }

    node.Next = list1
    if list1 == nil {
        node.Next = list2
    }

    return dummy.Next
}