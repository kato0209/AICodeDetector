
package main

import (
	"io/ioutil"
	"log"
)

func main() {
	data, err := ioutil.ReadFile("path/to/your/file.txt")
	if err != nil {
		log.Fatal(err)
	}
	
	// Use data
	_ = data
}
