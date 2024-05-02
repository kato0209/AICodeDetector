
package main

import (
	"fmt"
)

func compareStrings(str1, str2 string) bool {
	return str1 == str2
}

func main() {
	fmt.Println(compareStrings("hello", "world")) // false
	fmt.Println(compareStrings("go", "go"))       // true
}
