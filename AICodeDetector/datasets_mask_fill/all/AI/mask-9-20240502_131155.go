
package main

import (
	"fmt"
	"os"
)

func appendToFile(filename, text <extra_id_0> {
	f, err := os.OpenFile(filename, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if <extra_id_1> nil {
		return err
	}
	defer f.Close()

	if _, err := f.WriteString(text); err != nil {
		return err
	}
	return nil
}

func main() {
	err := appendToFile("example.txt", "This is the text to append.\n")
	if err <extra_id_2> {
		fmt.Println(err)
	}
}
