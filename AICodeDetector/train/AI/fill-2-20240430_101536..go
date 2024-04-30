package main

import (
	"fmt"
	"io/ioutil"
	"log"
)

func main() {
	// Replace 'example.txt' with the path relative to actual output directory.
	filename := "example.txt"

	content, err := ioutil.ReadFile(filename)
	if err != nil {
		log.Fatalf("Failed to read file: %s", err)
	}

	fmt.Printf("File content:\n%s", content)
}
