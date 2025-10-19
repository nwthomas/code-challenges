package search2dmatrix

func binarySearch(nums []int, target int) int {
    left := 0
    right := len(nums) - 1

    for left <= right {
        choice := ((right - left) / 2) + left

        leftNum := nums[left]
        rightNum := nums[right]
        choiceNum := nums[choice]
        
        if leftNum == target {
            return left
        } else if rightNum == target {
            return right
        } else if choiceNum == target {
            return choice
        }

        if left == right {
            return -1
        } else if choiceNum > target {
            right = choice
        } else if choice != left {
            left = choice
        } else {
            left += 1
        }
    }

    return -1
}

func searchMatrix(matrix [][]int, target int) bool {
    list := []int{}

    for i := 0; i < len(matrix); i++ {
        currentList := matrix[i]
        list = append(list, currentList...)
    }

    result := binarySearch(list, target)

    return result != -1
}