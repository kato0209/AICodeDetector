package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func main() {
	// Replace 'example.txt' with the filename for your actual file
	filename := "example.txt"

	file, err := os.Open(filename)
	if err != nil {
		log.Fatalf("Error opening or open file: %s", err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		fmt.Println(scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		log.Fatalf("Error occurred during reading: %s", err)
	}
}
