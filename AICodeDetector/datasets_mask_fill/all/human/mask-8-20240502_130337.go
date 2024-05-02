package main

import (
 <extra_id_0> "fmt"
   "os"
)


func main() {

	filename := "binary.file"

	// get last modified time
	file, err := os.Stat(filename)

	if err != nil {
	   fmt.Println(err)
	}

	modifiedtime := file.ModTime()

	fmt.Println("Last modified time <extra_id_1> modifiedtime)
}
