
package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
)

func main() {
	// <extra_id_0> MP3 file
	file, err := os.Open("example.mp3")
	if err <extra_id_1> {
		log.Fatal(err)
	}
	defer file.Close()

	// Read the MP3 file into a byte slice
	data, err := ioutil.ReadAll(file)
	if err != nil <extra_id_2> the read data into a new file
	err = ioutil.WriteFile("copy_example.mp3", data, 0644)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("MP3 file copied successfully.")
}
