package main

import (
	"fmt"
	"strings"
)

func compareStrings(str1, str2 string) bool {
	return strings.Compare(str1, str2) == 0
}

func main() {
	string1 := "Hello"
	string2 := "Hello"

	isEqual := compareStrings(string1, string2)
	fmt.Println(isEqual)
}