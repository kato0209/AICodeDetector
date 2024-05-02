
package main

import (
	"fmt"
	"io/ioutil"
	"log"
)

func main() {
	files, err := ioutil.ReadDir(".")
	if err != nil <extra_id_0> file := range files {
		fmt.Println(file.Name())
	}
}
