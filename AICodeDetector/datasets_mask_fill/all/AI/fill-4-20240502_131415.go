
package main

import (
	"log"
	"os"
)

func main() {
	content := []byte("Hello, Gophers!")
	err := os.Chmod("bogusfile.txt", 0644)
	if err != nil {
		log.Fatal(err)
	}
}
