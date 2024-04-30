package main

import (
	"fmt"
	"log"
	"path/filepath"
)

func main() {
	// Replace 'your/directory/path' with actual directory path
	rootPath := "your/directory/path"

	err := filepath.Walk(rootPath, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}
		if !info.IsDir() {
			fmt.Println(path)
		}
		return nil
	})

	if err != nil {
		log.Fatalf("Failed to walk through directory: %s", err)
	}
}

