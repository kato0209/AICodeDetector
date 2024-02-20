
package main

import (
	"fmt"
	"strings"
)

func compareStrings(str1, str2 string) bool {
	if strings.Compare(str1, str2) == 0 {
		return true
	} else {
		return false
	}
}

func main() {
	string1 := "hello"
	string2 := "world"
	result := compareStrings(string1, string2)
	fmt.Println(result)
}
