package main

import (
	"fmt"
	"log"
	"os"
)

func main() {
	filename := "example.txt"

	fileInfo, err := os.Stat(filename)
	if err != nil {
		log.Fatalf("Error getting file information: %s", err)
	}

	modifiedTime := fileInfo.ModTime()
	fmt.Printf("Last modified time of %s: %s\n", filename, modifiedTime)
}
