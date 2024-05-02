
package main

import (
	"io"
	"os"
)

func main() {
	sourceFile, err := os.Open("source.txt")
	if err != nil {
		panic(err)
	}
	defer sourceFile.Close()

	destinationFile, err := os.Create("destination.txt")
	if err != nil {
		panic(err)
	}
	defer destinationFile.Close()

	_, err = io.Copy(destinationFile, sourceFile)
	if err != nil {
		panic(err)
	}
}
