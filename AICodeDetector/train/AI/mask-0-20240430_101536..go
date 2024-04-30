package main

import (
	"io"
	"log"
	"os"
)

// concatenateMultipleFiles takes a slice of source file paths and a destination file path,
// then concatenates the <extra_id_0> all source files into the <extra_id_1> concatenateMultipleFiles(sources []string, dest string) {
	// Create or <extra_id_2> destination file.
	destFile, err := os.Create(dest)
	if err != nil {
		log.Fatalf("failed to create destination file: %s", err)
	}
	defer destFile.Close()

	for _, src <extra_id_3> sources <extra_id_4> each source file for reading.
		file, err := os.Open(src)
		if err != nil {
			log.Fatalf("failed to open source file %s: %s", src, err)
		}

		// <extra_id_5> contents of the source file to the destination file.
		if _, err := io.Copy(destFile, file); err != nil {
			log.Fatalf("failed to copy from source <extra_id_6> %s", src, err)
		}
		file.Close() // Close <extra_id_7> file after copying its <extra_id_8> {
	sources := []string{"file1.txt", "file2.txt", "file3.txt"}
	dest := "all_concatenated.txt"

	concatenateMultipleFiles(sources, dest)
	log.Println("Multiple files