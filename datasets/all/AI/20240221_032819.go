package main

import (
	"fmt"
	"strings"
)

func CompareStrings(str1, str2 string) bool {
	return strings.Compare(str1, str2) == 0
}

func main() {
	str1 := "hello"
	str2 := "world"

	result := CompareStrings(str1, str2)
	fmt.Println(result)
}