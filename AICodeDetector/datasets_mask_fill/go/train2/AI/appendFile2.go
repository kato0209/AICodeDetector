package main

import (
	"io/ioutil"
	"log"
)

func main() {
	text := "Hello, world! This is some text that we're writing to a file."
	filename := "example.txt"

	// Write the text to a new file. If the file doesn't exist, it will be created.
	// If it exists, it will be overwritten.
	err := ioutil.WriteFile(filename, []byte(text), 0644)
	if err != nil {
		log.Fatalf("Failed to write to file: %s", err)
	}

	log.Println("File written successfully.")
}
