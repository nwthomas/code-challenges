package powxy

func absolute(n int) int {
    if n < 0 {
        return -n
    }

    return n
}

func myPow(x float64, n int) float64 {
    total := 1.00000

    for i := 1; i <= absolute(n); i++ {
        if n > 0.00000 {
            total = total * x
        } else {
            total = total / x
        }
    }

    return total
}
