
package main

import (
	"log"
	"os"
)

func main() {
	content := []byte("Hello, Gophers!")
	err := os.WriteFile("example.txt", content, 0644)
	if err != nil {
		log.Fatal(err)
	}
}
