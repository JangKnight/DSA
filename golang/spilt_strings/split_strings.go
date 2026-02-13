package main

import "fmt"

func split_strs(str string) []string {
	var outArr []string

	if len(str)%2 != 0 {
		str += "_"
	}

	for i := 0; i < len(str)-1; i += 2 {
		outArr = append(outArr, str[i:i+2])
	}

	return outArr

}

func main() {
	inArr := [...]string{"abc", "dawsd", "awsaws"}

	for _, str := range inArr {
		fmt.Println(split_strs(str))
	}
}
