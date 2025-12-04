package palindromepartitioning

func partition(s string) [][]string {
	result := [][]string{}
	part := []string{}

	var isPalindrome = func(s string, l int, r int) bool {
		for l < r {
			if s[l] != s[r] {
				return false
			}
			l += 1
			r -= 1
		}

		return true
	}

	var dfs func(int)
	dfs = func(i int) {
		if i >= len(s) {
			newPart := make([]string, len(part))
			copy(newPart, part)
			result = append(result, newPart)
			return
		}

		for j := i; j < len(s); j++ {
			if isPalindrome(s, i, j) {
				part = append(part, s[i:j+1])
				dfs(j + 1)
				part = part[:len(part)-1]
			}
		}
	}

	dfs(0)

	return result
}
