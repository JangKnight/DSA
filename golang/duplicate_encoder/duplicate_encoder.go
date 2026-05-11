package main

import (
	"fmt"
	"strings"
)

func main() {
	words := []string{"din", "recede", "Success", "(( @"}
	for _, word := range words {
		fmt.Println(DuplicateEncode(word))
	}
}

func DuplicateEncode(word string) string {
	arr := []rune{}

	lowercasedWord := strings.ToLower(word)

	for _, currentRune := range lowercasedWord {
		count := strings.Count(lowercasedWord, string(currentRune))
		if count > 1 {
			arr = append(arr, ')')
		} else {
			arr = append(arr, '(')
		}
	}

	return string(arr)
}
