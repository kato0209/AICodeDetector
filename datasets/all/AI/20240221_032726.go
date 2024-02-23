package main

import (
	"fmt"
	"strings"
)

func compareStrings(str1, str2 string) bool {
	return strings.Compare(str1, str2) == 0
}

func main() {
	fmt.Println(compareStrings("hello", "hello")) // Output: true
}