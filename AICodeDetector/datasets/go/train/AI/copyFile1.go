package main

import (
	"io/ioutil"
	"log"
)

// copyFileSimple reads the entire source file into memory and writes it to the destination file.
// This method is straightforward but not suitable for large files.
func copyFileSimple(src, dst string) error {
	data, err := ioutil.ReadFile(src)
	if err != nil {
		return err
	}

	err = ioutil.WriteFile(dst, data, 0644)
	if err != nil {
		return err
	}

	return nil
}

func main() {
	src := "source.txt"
	dst := "destination_simple.txt"

	if err := copyFileSimple(src, dst); err != nil {
		log.Fatalf("Failed to copy file: %s", err)
	}

	log.Println("File copied successfully using ioutil.")
}
