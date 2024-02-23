
package main

import (
	"fmt"
	"strings"
)

func compareStrings(str1, str2 string) bool {
	return strings.Compare(str1, str2) == 0
}

func main() {
	str1 := "hello"
	str2 := "world"
	fmt.Println(compareStrings(str1, str2))
}
