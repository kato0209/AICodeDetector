
package main

import (
	"fmt"
	"os"
)

func main() {
	data := []byte("Hello, Gophers!\n")
	err := writeFile("test-data", data, 0644)
	if err != nil {
		fmt.Printf("Error writing file: %s\n", err)
	}
}
