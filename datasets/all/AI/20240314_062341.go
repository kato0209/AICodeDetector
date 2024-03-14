
package main

import (
	"fmt"
	"os"
	"time"
)

func main() {
	filePath := "your-file-path-here"
	fileInfo, err := os.Stat(filePath)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}
	modTime := fileInfo.ModTime()
	fmt.Println("Last modified time:", modTime.Format(time.RFC1123))
}
