
package main

import (
	"fmt"
	"strings"
)

func compareStrings(s1, s2 string) bool {
	return strings.Compare(s1, s2) == 0
}

func main() {
	s1 := "hello"
	s2 := "world"
	fmt.Println(compareStrings(s1, s2))
}
