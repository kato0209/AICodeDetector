package main

import (
	"fmt"
	"io/ioutil"
)

func main() {
	bytes, err := ioutil.ReadFile("sample.txt")
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println(string(bytes))
}
