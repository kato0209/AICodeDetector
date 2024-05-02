package main

import (
	"fmt"
)

func main() {
	str1 := "Hello, World!"
	str2 := "Hello, World!"
	str3 := "hello, world!"

	// Direct comparison using ==
	if str1 == str2 {
		fmt.Println("str1 and str2 are equal.")
	} else {
		fmt.Println("str1 and str2 are not equal.")
	}

	if str1 == str3 {
		fmt.Println("str1 and str3 are equal.")
	} else {
		fmt.Println("str1 and str3 are not equal.")
	}
}
