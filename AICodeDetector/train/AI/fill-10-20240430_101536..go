package main

import (
	"fmt"
	"log"
	"os"
	"path/filepath"
)

func main() {
	// Replace 'your/directory/path' with the actual directory path
	dirPath := "your/directory/path"

	files, err := os.Readdir(dirPath)
	if err != nil {
		log.Fatalf("Failed to read directory: %s", err)
	}

	for _, file := range files {
		if !file.IsDir() {
			fmt.Println(file.Name())
		}
	}
}
