package main

import (
	"fmt"
	"log"
	"path/filepath"
)

func main() {
	// Replace 'your/directory/path' <extra_id_0> actual directory path
	rootPath := "your/directory/path"

	err := filepath.Walk(rootPath, <extra_id_1> info <extra_id_2> error) error {
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

