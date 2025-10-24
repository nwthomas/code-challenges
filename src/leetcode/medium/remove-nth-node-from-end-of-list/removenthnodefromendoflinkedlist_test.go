package removenthnodefromendoflist

import (
	"reflect"
	"testing"
)

func TestRemoveNthFromEnd(t *testing.T) {
	tests := []struct {
		name string
		head *ListNode
		n    int
		want *ListNode
	}{
		{
			name: "test 1",
			head: &ListNode{Val: 1, Next: &ListNode{Val: 2, Next: &ListNode{Val: 3, Next: &ListNode{Val: 4, Next: &ListNode{Val: 5}}}}},
			n: 2,
			want: &ListNode{Val: 1, Next: &ListNode{Val: 2, Next: &ListNode{Val: 3, Next: &ListNode{Val: 5}}}},
		},
		{
			name: "test 2",
			head: &ListNode{Val: 1},
			n: 1,
			want: nil,
		},
		{
			name: "test 3",
			head: &ListNode{Val: 1, Next: &ListNode{Val: 2}},
			n: 2,
			want: &ListNode{Val: 2},
		},
	}
	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			result := removeNthFromEnd(test.head, test.n)
			if !reflect.DeepEqual(result, test.want) {
				t.Errorf("removeNthFromEnd(%v, %d) = %v, want %v", test.head, test.n, result, test.want)
			}
		})
	}
}