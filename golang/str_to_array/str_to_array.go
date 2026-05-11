package main

import "strings"

func StringToArray(str string) []string {
      outArr := strings.Split(str, " ")
      return outArr
}
