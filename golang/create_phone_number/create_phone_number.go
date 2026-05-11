package main

import "strconv"

func CreatePhoneNumber(numbers [10]uint) string {
	//p = phoneNumber; made short to concat final string
	p := []string{}
	for _, number := range numbers {
		strNum := strconv.FormatUint(uint64(number), 10)
		p = append(p, strNum)
	}

	return "(" + p[0] + p[1] + p[2] + ")" + " " + p[3] + p[4] + p[5] + "-" + p[6] + p[7] + p[8] + p[9]
}

func main() {
	println(CreatePhoneNumber([10]uint{1, 2, 3, 4, 5, 6, 7, 8, 9, 0}))
	println(CreatePhoneNumber([10]uint{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}))
	println(CreatePhoneNumber([10]uint{9, 8, 7, 6, 5, 4, 3, 2, 1, 0}))
}

//BEST PRACTICE SOLUTION
// import "fmt"

// func CreatePhoneNumber(n [10]uint) string {
//   return fmt.Sprintf("(%d%d%d) %d%d%d-%d%d%d%d", n[0], n[1], n[2], n[3], n[4], n[5], n[6], n[7], n[8], n[9])
// }
