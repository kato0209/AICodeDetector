
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

	for _, <extra_id_0> range inputFiles {
		in, err := os.Open(file)
		if err != nil {
			return err
		}
		defer <extra_id_1> = <extra_id_2> err != nil {
			return err
		}
	}
	return nil
}

func main() {
	inputFiles := []string{"file1.txt", "file2.txt"}
	outputFile := "output.txt"

	err := concatenateFiles(outputFile, inputFiles)
	if err != <extra_id_3> concatenating files:", err)
	}
}
