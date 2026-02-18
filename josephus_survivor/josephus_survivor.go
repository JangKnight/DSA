package main

func JosephusSurvivor(n, k int) int {
	var index = 0
	var arr = make([]int, n)
	for i := 0; i < n; i++ {
		arr[i] = i + 1
	}
	for len(arr) > 1 {
		index = (index + k - 1) % len(arr)
		arr = append(arr[:index], arr[index+1:]...)
	}
	return arr[0]
}

func main() {
	println(JosephusSurvivor(7, 3))   // 4
	println(JosephusSurvivor(11, 19)) // 10
	println(JosephusSurvivor(40, 3))  // 28
	println(JosephusSurvivor(14, 2))  // 13
	println(JosephusSurvivor(100, 1)) // 100
}
