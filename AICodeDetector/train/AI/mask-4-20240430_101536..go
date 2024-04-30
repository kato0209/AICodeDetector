package main

import (
	"log"
	"os"
)

func appendToFile(filename, text string) {
	// Open <extra_id_0> in <extra_id_1> If it doesn't exist, create it with <extra_id_2> err := os.OpenFile(filename, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err <extra_id_3> {
		log.Fatalf("failed to open file: %s", err)
	}
	defer file.Close()

	// Write the text to the file.
	if _, err := file.WriteString(text + "\n"); err != nil {
		log.Fatalf("failed to write to file: %s", err)
	}
}

func main() {
	appendToFile("example.txt", "Hello, <extra_id_4> a new line of text!")
	log.Println("Text appended successfully.")
}
