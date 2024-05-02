
package main

import (
	"io/ioutil"
	"log"
)

func main() {
	data, <extra_id_0> ioutil.ReadFile("path/to/your/file.txt")
	if err != nil {
		log.Fatal(err)
	}
	
	// Use data
	_ = data
}
