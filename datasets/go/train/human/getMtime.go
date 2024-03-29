package main

import (
   "fmt"
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

	fmt.Println("Last modified time : ", modifiedtime)
}
