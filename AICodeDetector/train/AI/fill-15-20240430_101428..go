package main

import (
	"log"
	"os"
)

func appendToFile(filename, text string) {
	// Open the file in append mode. If it doesn't exist, create it with permissions 0644.
	file, err := os.OpenFile(filename, os.O_RDWR|os.O_APPEND, 0644)
	if err != nil {
		log.Fatalf("Failed to open file: %s", err)
	}
	defer file.Close()

	// Write the text to the file.
	if _, err := file.WriteString(text + "\n"); err!= nil {
		log.Fatalf("Failed to append text to file: %s", err)
	}

	log.Println("Text appended to file successfully.")
}

func main() {
	text := "This is another line of text."
	filename := "example.txt"

	appendToFile(filename, text)
}
