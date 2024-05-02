
package main

import (
	"fmt"
	"os"
)

func appendToFile(filename, text string) error {
	f, err := os.OpenFile(filename, os.O_APPEND|os.O_WRONLY, 0644)
	if err != nil {
		return err
	}
	defer f.Close()

	_, err = f.WriteString(text)
	return err
}

func main() {
	err := appendToFile("example.txt", "Appended text\n")
	if err != nil {
		fmt.Println("Error appending to file:", err)
	}
}
