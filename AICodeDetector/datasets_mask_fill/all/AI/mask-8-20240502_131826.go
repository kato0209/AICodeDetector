
package main

import (
	"fmt"
	"os"
	"time"
)

func main() {
	filename := "your_file.txt" // Specify your file name <extra_id_0> := os.Stat(filename)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}
	modTime := info.ModTime()
	fmt.Println("Last modified time:", modTime.Format(time.RFC1123))
}
