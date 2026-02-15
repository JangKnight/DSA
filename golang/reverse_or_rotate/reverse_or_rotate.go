package main

import (
	"strconv"
	"strings"
)

func Revrot(s string, n int) string {

	dataArray := []string{}

	if n <= 0 || s == "" || n > len(s) {
		return ""
	}

	for i, j := n, 0; i <= len(s); i += n {
		dataArray = append(dataArray, s[j:i])
		j = i
	}

	for i, chunk := range dataArray {
		sum := 0

		for _, letter := range chunk {
			num, _ := strconv.ParseInt(string(letter), 10, 64)
			sum += int(num)
		}

		if sum%2 == 0 {
			//reverse chunk
			chars := []rune(chunk)
			for i, j := 0, len(chars)-1; i < j; i, j = i+1, j-1 {
				chars[i], chars[j] = chars[j], chars[i]
			}
			chunk = string(chars)
		} else {
			//rotate chunk
			tail := chunk[:1]
			head := chunk[1:]
			chunk = string(head) + string(tail)
		}

		dataArray[i] = chunk
	}

	return strings.Join(dataArray, "")

}

func main() {
	println(Revrot("1234", 0))
	println(Revrot("", 0))
	println(Revrot("1234", 5))
	println(Revrot("1234", 4))
	println(Revrot("123456987654", 6))
	println(Revrot("66443875", 4))
	println(Revrot("66443875", 8))
	println(Revrot("664438769", 8))
}
