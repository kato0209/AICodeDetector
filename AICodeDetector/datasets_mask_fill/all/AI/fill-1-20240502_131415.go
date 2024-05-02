
package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
)

func main() {
	// Open the MP3 file
	file, err := os.Open("yourfile.mp3")
	if err!= nil {
		log.Fatal(err)
	}
	defer file.Close()

	// Read the file's bytes
	data, err := ioutil.ReadAll(file)
	if err != nil {
		log.Fatal(err)
	}

	// For demonstration, just show the size of the MP3 file
	fmt.Println("Size of MP3 file:", len(data), "bytes")
}
