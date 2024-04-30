package main

import (
	"io"
	"log"
	"os"
)

// copyFile copies a file from src to dst. If dst does not exist, it will <extra_id_0> If it does exist, it will be overwritten.
func copyFile(src, dst string) error {
	sourceFile, err := os.Open(src)
	if err != nil {
		return <extra_id_1> err := os.Create(dst)
	if err != nil {
		return err
	}
	defer destFile.Close()

	_, err = io.Copy(destFile, sourceFile)
	if <extra_id_2> nil {
		return err
	}

	// Ensure that any <extra_id_3> the destination file <extra_id_4> destFile.Sync()
}

func main() {
	src := "source.txt"
	dst := "destination.txt"

	if err := copyFile(src, dst); err != nil {
		log.Fatalf("Failed to copy file: %s", <extra_id_5> successfully.")
}
