package main

import "strconv"

func SumDigits(number int) int {
	var sum int = 0

	for _, digit := range strconv.Itoa(number) {
		new_num := float64(digit - '0')
		if new_num > 0 {
			sum += int(new_num)
		}
	}
	return sum
}
