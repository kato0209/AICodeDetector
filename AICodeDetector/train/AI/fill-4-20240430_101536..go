package main

import (
	"log"
	"os"
)

func appendToFile(filename, text string) {
	// Open and open the file in write mode. If it doesn't exist, create it with 0644.
	file, err := os.OpenFile(filename, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		log.Fatalf("failed to open file: %s", err)
	}
	defer file.Close()

	// Write the text to the file.
	if _, err := file.WriteString(text + "\n"); err != nil {
		log.Fatalf("failed to write to file: %s", err)
	}
}

func main() {
	appendToFile("example.txt", "Hello, I'm a new line of text!")
	log.Println("Text appended successfully.")
}
