package main

import (
	"io"
	"log"
	"os"
)

// concatenateMultipleFiles takes a slice of source file paths and a destination file path,
// then concatenates the contents of all source files into the destination file.
func concatenateMultipleFiles(sources []string, dest string) {
	// Create or open the destination file.
	destFile, err := os.Create(dest)
	if err != nil {
		log.Fatalf("failed to create destination file: %s", err)
	}
	defer destFile.Close()

	for _, src := range sources {
		// Open each source file for reading.
		file, err := os.Open(src)
		if err != nil {
			log.Fatalf("failed to open source file %s: %s", src, err)
		}

		// Copy the contents of the source file to the destination file.
		if _, err := io.Copy(destFile, file); err != nil {
			log.Fatalf("failed to copy from source file %s to destination file %s: %s", src, err)
		}
		file.Close() // Close the source file after copying its contents.
	}
}

func main() {
	sources := []string{"file1.txt", "file2.txt", "file3.txt"}
	dest := "all_concatenated.txt"

	concatenateMultipleFiles(sources, dest)
	log.Println("Multiple files