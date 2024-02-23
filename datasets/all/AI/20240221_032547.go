
package main

import (
	"fmt"
	"strings"
)

func compareTwoStrings(str1, str2 string) bool {
	return strings.Compare(str1, str2) == 0
}

func main() {
	string1 := "hello"
	string2 := "world"
	result := compareTwoStrings(string1, string2)
	fmt.Println(result)
}
