
package main

import (
	"fmt"
	"io"
	"os"
)

func concatenateFiles(outputFile string, inputFiles []string) error {
	out, err := os.Create(outputFile)
	if err != nil {
		return err
	}
	defer out.Close()

	for _, file := range inputFiles {
		in, err := os.Open(file)
		if err != nil {
			return err
		}
		defer in.Close()
		_, err = io.Copy(out, in)
		if err != nil {
			return err
		}
	}
	return nil
}

func main() {
	inputFiles := []string{"file1.txt", "file2.txt"}
	outputFile := "output.txt"

	err := concatenateFiles(outputFile, inputFiles)
	if err != nil {
		return fmt.Errorf("Error concatenating files:", err)
	}
}
