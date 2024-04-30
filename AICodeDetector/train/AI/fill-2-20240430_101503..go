package main

import (
	"io"
	"log"
	"os"
)

// concatenateFiles takes two source file paths and a destination file path,
// then concatenates the contents of the first and second source files into the // destination file.
func concatenateFiles(src1, src2, dest string) {
	// Open the first source file for reading.
	file1, err := os.Open(src1)
	if err != nil {
		log.Fatalf("failed to open first file: %s", err)
	}
	defer file1.Close()

	// Open the second source file for reading.
	file2, err := os.Open(src2)
	if err != nil {
		log.Fatalf("failed to open second file: %s", err)
	}
	defer file2.Close()

	// Create the destination file.
	destFile, err := os.Create(dest)
	if err != nil {
		log.Fatalf("failed to create destination file: %s", err)
	}
	defer destFile.Close()

	// Copy the contents of the first file into the destination file.
	if _, err := io.Copy(destFile, file1); err != nil {
		log.Fatalf("failed to copy first file: %s", err)
	}

	// Copy the contents of the second file into the destination file.
	if