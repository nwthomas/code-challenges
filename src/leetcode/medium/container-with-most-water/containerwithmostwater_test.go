package containerwithmostwater

import (
	"testing"
)

func TestContainerWithMostWater(t *testing.T) {
	tests := []struct {
		name string
		heights []int
		want int
	}{
		{name: "test 1", heights: []int{1,8,6,2,5,4,8,3,7}, want: 49},
		{name: "test 2", heights: []int{1,1}, want: 1},
		{name: "test 3", heights: []int{1,2,1}, want: 2},
		{name: "test 4", heights: []int{1,2,3,4,5,6,7,8,9,10}, want: 25},
		{name: "test 5", heights: []int{10,9,8,7,6,5,4,3,2,1}, want: 25},
		{name: "test 6", heights: []int{1,1,1,1,1,1,1,1,1,1}, want: 9},
	}
	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			got := containerWithMostWater(test.heights)
			if got != test.want {
				t.Errorf("containerWithMostWater(%v) = %d, want %d", test.heights, got, test.want)
			}	
		})
	}
}

// Benchmark tests for performance testing
func BenchmarkContainerWithMostWater(b *testing.B) {
	heights := []int{1,8,6,2,5,4,8,3,7,1,8,6,2,5,4,8,3,7}
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		containerWithMostWater(heights)
	}
}

func BenchmarkContainerWithMostWaterSmall(b *testing.B) {
	heights := []int{1,1}
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		containerWithMostWater(heights)
	}
}