package main

/*
Complete the solution so that it splits the string into
strings of two characters in a list/array (depending on the language you use).
If the string contains an odd number of characters
then it should replace the missing second character of the final pair with
an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
*/

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
