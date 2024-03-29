package main

import (
	"io"
	"log"
	"os"
)

// copyFile copies a file from src to dst. If dst does not exist, it will be created.
// If it does exist, it will be overwritten.
func copyFile(src, dst string) error {
	sourceFile, err := os.Open(src)
	if err != nil {
		return err
	}
	defer sourceFile.Close()

	destFile, err := os.Create(dst)
	if err != nil {
		return err
	}
	defer destFile.Close()

	_, err = io.Copy(destFile, sourceFile)
	if err != nil {
		return err
	}

	// Ensure that any writes to the destination file are committed.
	return destFile.Sync()
}

func main() {
	src := "source.txt"
	dst := "destination.txt"

	if err := copyFile(src, dst); err != nil {
		log.Fatalf("Failed to copy file: %s", err)
	}

	log.Println("File copied successfully.")
}
