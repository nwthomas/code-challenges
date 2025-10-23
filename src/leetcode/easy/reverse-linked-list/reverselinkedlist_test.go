package reverselinkedlist

import (
	"reflect"
	"testing"
)

func TestReverseList(t *testing.T) {
	tests := []struct {
		name string
		head *ListNode
		want *ListNode
	}{
		{
			name: "empty list", 
			head: nil, 
			want: nil,
		},
		{
			name: "single node", 
			head: &ListNode{Val: 1}, 
			want: &ListNode{Val: 1},
		},
		{
			name: "two nodes", 
			head: &ListNode{Val: 1, Next: &ListNode{Val: 2}}, 
			want: &ListNode{Val: 2, Next: &ListNode{Val: 1}},
		},
		{
			name: "ten nodes", 
			head: &ListNode{Val: 1, Next: &ListNode{Val: 2, Next: &ListNode{Val: 3, Next: &ListNode{Val: 4, Next: &ListNode{Val: 5, Next: &ListNode{Val: 6, Next: &ListNode{Val: 7, Next: &ListNode{Val: 8, Next: &ListNode{Val: 9, Next: &ListNode{Val: 10}}}}}}}}}}, 
			want: &ListNode{Val: 10, Next: &ListNode{Val: 9, Next: &ListNode{Val: 8, Next: &ListNode{Val: 7, Next: &ListNode{Val: 6, Next: &ListNode{Val: 5, Next: &ListNode{Val: 4, Next: &ListNode{Val: 3, Next: &ListNode{Val: 2, Next: &ListNode{Val: 1}}}}}}}}}},
		},
	}
	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			result := reverseList(test.head)
			if !reflect.DeepEqual(result, test.want) {
				t.Errorf("reverseList(%v) = %v, want %v", test.head, result, test.want)
			}
		})
	}
}