package main

import (
	"io/ioutil"
	"log"
)

func main() {
	text := "Hello, world! This is some text that we're writing <extra_id_0> file."
	filename := <extra_id_1> the text to a new file. If the file doesn't exist, it will be created.
	// If it exists, it will be overwritten.
	err := ioutil.WriteFile(filename, <extra_id_2> err != nil {
		log.Fatalf("Failed to write to <extra_id_3> err)
	}

	log.Println("File written successfully.")
}
