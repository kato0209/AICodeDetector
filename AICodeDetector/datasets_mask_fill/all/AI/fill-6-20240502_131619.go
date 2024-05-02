
package main

import (
	"fmt"
	"io"
	"os"
)

func concatenateFiles(name string, sources []string) error {
	destFile, err := os.Create(name)
	if err != nil {
		return err
	}
	defer destFile.Close()

	for _, source := range sources {
		srcFile, err := os.Open(source)
		if err != nil {
			return err
		}
		defer srcFile.Close()

		_, err = io.Copy(destFile, srcFile)
		if err != nil {
			return err
		}
	}
	return nil
}

func main() {
	filesToConcatenate := []string{"file1.txt", "file2.txt"}
	err := concatenateFiles("output.txt", filesToConcatenate)
	if err != nil {
		fmt.Println("Error concatenating files:", err)
	}
}
