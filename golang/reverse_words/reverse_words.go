package main

import (
	"fmt"
	"strings"
)

var sentence string = "The quick brown fox jumps over the lazy dog."

func main() {
	fmt.Print(reverse(sentence))
}

func reverse(phrase string) (str string) {
	split_phrase := strings.Split(phrase, " ")
	for i, word := range split_phrase {
		letters := []rune(word)
		for x, y := 0, len(letters)-1; x < y; x, y = x+1, y-1 {
			letters[x], letters[y] = letters[y], letters[x]
		}
		split_phrase[i] = string(letters)
	}
	return strings.Join(split_phrase, " ")
}
