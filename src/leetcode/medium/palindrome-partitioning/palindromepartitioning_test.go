package palindromepartitioning

import (
	"reflect"
	"testing"
)

func TestPartition(t *testing.T) {
	tests := []struct {
		name     string
		input    string
		expected [][]string
	}{
		{name: "aab", input: "aab", expected: [][]string{{"a", "a", "b"}, {"aa", "b"}}},
		{name: "a", input: "a", expected: [][]string{{"a"}}},
		{name: "abc", input: "abc", expected: [][]string{{"a", "b", "c"}}},
	}
	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			got := partition(test.input)
			if !reflect.DeepEqual(got, test.expected) {
				t.Errorf("partition(%s) = %v, want %v", test.input, got, test.expected)
			}
		})
	}
}
