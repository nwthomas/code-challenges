package mergetwosortedlists

import (
	"reflect"
	"testing"
)

func TestMergeTwoLists(t *testing.T) {
	tests := []struct {
		name string
		list1 *ListNode
		list2 *ListNode
		expected *ListNode
	}{
		{
			name: "test 1", 
			list1: &ListNode{Val: 1, Next: &ListNode{Val: 2, Next: &ListNode{Val: 4}}}, 
			list2: &ListNode{Val: 1, Next: &ListNode{Val: 3, Next: &ListNode{Val: 4}}},
			expected: &ListNode{Val: 1, Next: &ListNode{Val: 1, Next: &ListNode{Val: 2, Next: &ListNode{Val: 3, Next: &ListNode{Val: 4, Next: &ListNode{Val: 4}}}}}}},
		{
			name: "test 2", 
			list1: nil, 
			list2: nil, 
			expected: nil,
		},
		{
			name: "test 3", 
			list1: nil, 
			list2: &ListNode{Val: 0}, 
			expected: &ListNode{Val: 0},
		},
		{
			name: "test 4", 
			list1: &ListNode{Val: 1},
			list2: nil,
			expected: &ListNode{Val: 1},
		},
	}
	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			result := mergeTwoLists(test.list1, test.list2)
			if !reflect.DeepEqual(result, test.expected) {
				t.Errorf("Expected %v, got %v", test.expected, result)
			}
		})
	}
}