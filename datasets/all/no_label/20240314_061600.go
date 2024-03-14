
package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
)

func main() {
	// Open the MP3 file
	file, err := os.Open("example.mp3")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	// Read the MP3 file into a byte slice
	data, err := ioutil.ReadAll(file)
	if err != nil {
		log.Fatal(err)
	}

	// Save the read data into a new file
	err = ioutil.WriteFile("copy_example.mp3", data, 0644)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("MP3 file copied successfully.")
}
