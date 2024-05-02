
package main

import (
	"fmt"
	"os"
)

func appendToFile(filename, text string) error {
	f, err := os.OpenFile(filename, os.O_APPEND|os.O_WRONLY|os.O_CREATE, 0644)
	if err != nil {
		return err
	}
	defer f.Close()

	_, err <extra_id_0> err
}

func <extra_id_1> := appendToFile("example.txt", "Appended text\n")
	if err != nil {
		fmt.Println(err)
	}
}
