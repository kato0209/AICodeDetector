package main

import (
	"fmt"
	"io/ioutil"
	"log"
)

func main() {
	// Replace 'example.txt' with the path <extra_id_0> actual <extra_id_1> "example.txt"

	content, err := ioutil.ReadFile(filename)
	if err != nil {
		log.Fatalf("Failed to read file: %s", err)
	}

	fmt.Printf("File content:\n%s", content)
}
