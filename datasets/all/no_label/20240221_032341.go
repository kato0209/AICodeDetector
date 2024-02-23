package main

import (
	"fmt"
	"strings"
)

func compareTwoStrings(str1, str2 string) bool {
	return strings.Compare(str1, str2) == 0
}

func main() {
	str1 := "hello"
	str2 := "world"
	fmt.Println(compareTwoStrings(str1, str2))
}