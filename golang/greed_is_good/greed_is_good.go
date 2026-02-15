package main

var triplePointsMap = map[int]int{
	1: 1000,
	2: 200,
	3: 300,
	4: 400,
	5: 500,
	6: 600,
}

var regPointsMap = map[int]int{
	1: 100,
	5: 50,
}

func Score(dice [5]int) int {
	score := 0

	for num, points := range triplePointsMap {
		count := countChars(dice[:], num)
		if count >= 3 {
			score += points
			count -= 3
		}
		score += count * regPointsMap[num]
	}

	return score
}

func countChars(chars []int, num int) int {
	count := 0
	for _, c := range chars {
		if c == num {
			count++
		}
	}
	return count
}

func main() {
	println(Score([5]int{5, 1, 3, 4, 1}))
	println(Score([5]int{1, 1, 1, 3, 1}))
	println(Score([5]int{2, 4, 4, 5, 4}))
}
