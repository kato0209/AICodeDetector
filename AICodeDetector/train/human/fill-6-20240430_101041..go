package main

import (
	"fmt"
	"strings"
)

func main() {
	str := "abcawcwoca"
	result := strings.Replace(str, "a", "b", -1) // bawcwocaa
	fmt.Println(result) // bcwcwoca
}
