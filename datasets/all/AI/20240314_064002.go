
package main

import (
	"fmt"
	"io/ioutil"
	"log"
)

func main() {
	data, err := ioutil.ReadFile("path/to/your/file.txt")
	if err != nil {
		log.Fatal(err)
	}

	fmt.Print(string(data))
}
