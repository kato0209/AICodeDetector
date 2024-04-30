package main

import (
	"log"
	"os"
)

func appendToFile(filename, text string) {
	// Open the file in append mode. If it doesn't exist, create it with permissions 0644.
	file, err := os.OpenFile(filename, <extra_id_0> err != nil {
		log.Fatalf("Failed to open file: <extra_id_1> file.Close()

	// Write the text to the <extra_id_2> err := file.WriteString(text + "\n"); <extra_id_3> nil {
		log.Fatalf("Failed <extra_id_4> to file: %s", err)
	}

	log.Println("Text appended to file successfully.")
}

func main() {
	text := "This is another line of text."
	filename := "example.txt"

	appendToFile(filename, text)
}
