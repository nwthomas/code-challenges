package coinchange

import (
	"testing"
)

func TestCoinChange(t *testing.T) {
	tests := []struct {
		name   string
		coins  []int
		amount int
		want   int
	}{
		{
			name: "returns neg one if no change possible",
			coins: []int{7, 10, 15},
			amount: 5,
			want: -1,
		},
		{
			name: "returns zero if target is zero",
			coins: []int{1, 4, 5, 100},
			amount: 0,
			want: 0,
		},
		{
			name: "returns fewest coins for targeted amount",
			coins: []int{1, 3, 5, 8},
			amount: 100,
			want: 14,
		},
		{
			name: "handles coins of only one",
			coins: []int{1},
			amount: 1000,
			want: 1000,
		},
		{
			name: "returns neg one if only coins greater than amount",
			coins: []int{1000, 10000},
			amount: 10,
			want: -1,
		},
	}
	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			got := coinChange(test.coins, test.amount)
			if got != test.want {
				t.Errorf("coinChange(%v, %d) = %d, want %d", test.coins, test.amount, got, test.want)
			}
		})
	}
}