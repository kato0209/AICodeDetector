
package main

import (
	"fmt"
	"io"
	"os"
)

func <extra_id_0> sources []string) error {
	destFile, err <extra_id_1> err != nil {
		return err
	}
	defer destFile.Close()

	for _, source := range <extra_id_2> err := os.Open(source)
		if err != nil <extra_id_3> srcFile.Close()

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
