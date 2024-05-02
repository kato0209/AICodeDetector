
package main

import (
	"io"
	"os"
)

func main() {
	sourceFile, err := os.Open("source.txt")
	if <extra_id_0> nil <extra_id_1> err := os.Create("destination.txt")
	if err != nil {
		panic(err)
	}
	defer destinationFile.Close()

	_, err = io.Copy(destinationFile, sourceFile)
	if err != nil {
		panic(err)
	}
}
