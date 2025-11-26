package powxy

import (
	"testing"
)

func TestMyPow(t *testing.T) {
	tests := []struct {
		name string
		x    float64
		n    int
		want float64
 	} {
		{name: "test 1", x: 2.00000, n: 10, want: 1024.00000},
		{name: "test 2", x: 2.10000, n: 2, want: 4.41000},
		{name: "test 3", x: 2.00000, n: -2, want: 0.25000},
	}
	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			got := myPow(test.x, test.n)
			if got != test.want {
				t.Errorf("myPow(%f, %d) = %f, want %f", test.x, test.n, got, test.want)
			}
		})
	}
}