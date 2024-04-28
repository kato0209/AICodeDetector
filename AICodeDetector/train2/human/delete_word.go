package main

import (
	"fmt"
	"strings"
)

func main() {
	str := "abcawcwoca"
	result := strings.Replace(str, "a", "", 2)

	fmt.Println(result) // bcwcwoca
}
