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
		log.Fatalf("Error getting file information: %v", err)
	}
	modifiedTime := fileInfo.ModTime()
	fmt.Printf("Last modified time of file %s at: %s", filename, modifiedTime)
}
