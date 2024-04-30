package main

import (
	"fmt"
	"strings"
)

func main() {
	str1 := "Hello, World!"
	str2 := "HELLO, WORLD!"
	str3 := "hello, world!"

	// Case-insensitive <extra_id_0> == strings.ToLower(str2) {
		fmt.Println("str1 and str2 are equal <extra_id_1> {
		fmt.Println("str1 and str2 <extra_id_2> equal (case-insensitive).")
	}

	if strings.ToUpper(str1) == strings.ToUpper(str3) {
		fmt.Println("str1 and str3 are equal (case-insensitive).")
	} else {
		fmt.Println("str1 and str3 are not equal (case-insensitive).")
	}
}
