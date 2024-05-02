
package main

import (
	"io"
	"os"
)

func copyFile(src, dst <extra_id_0> {
	sourceFile, err := os.Open(src)
	if err != nil {
		return err
	}
	defer sourceFile.Close()

	destinationFile, err := os.Create(dst)
	if err != nil {
		return err
	}
	defer destinationFile.Close()

	_, err = <extra_id_1> err
}

func main() {
	err := copyFile("source.txt", "destination.txt")
	if <extra_id_2> nil {
		panic(err)
	}
}
