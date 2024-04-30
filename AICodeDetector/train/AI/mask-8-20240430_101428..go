package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func main() {
	// Replace 'example.txt' with the <extra_id_0> your actual file
	filename := "example.txt"

	file, err := <extra_id_1> != nil <extra_id_2> open file: %s", err)
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
