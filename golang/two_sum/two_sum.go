package main

// assumes input array (numbers) is sorted
func TwoSum(numbers []int, target int) [2]int {
	i, j := 0, len(numbers)-1

	for i < j {
		if numbers[i]+numbers[j] == target {
			return [2]int{i, j}
		} else if numbers[i]+numbers[j] < target {
			i++
		} else {
			j--
		}
	}
	return [2]int{}
}
