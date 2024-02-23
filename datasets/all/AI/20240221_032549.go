package main

import (
	"fmt"
	"strings"
)

func compareStrings(s1, s2 string) bool {
	return strings.Compare(s1, s2) == 0
}

func main() {
	str1 := "hello"
	str2 := "world"

	fmt.Println(compareStrings(str1, str2))
}