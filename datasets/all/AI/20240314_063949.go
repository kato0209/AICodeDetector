
package main

import (
	"fmt"
	"io"
	"os"
)

func main() {
	if len(os.Args) < 3 {
		fmt.Printf("Usage: %s destination_file source_file1 [source_file2 ...]\n", os.Args[0])
		os.Exit(1)
	}

	destFile, err := os.Create(os.Args[1])
	if err != nil {
		fmt.Println("Error creating destination file:", err)
		os.Exit(1)
	}
	defer destFile.Close()

	for _, sourceFileName := range os.Args[2:] {
		sourceFile, err := os.Open(sourceFileName)
		if err != nil {
			fmt.Println("Error opening source file:", err)
			os.Exit(1)
		}
		defer sourceFile.Close()

		_, err = io.Copy(destFile, sourceFile)
		if err != nil {
			fmt.Println("Error copying file:", err)
			os.Exit(1)
		}
	}
}
