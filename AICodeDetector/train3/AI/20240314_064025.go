
package main

import (
	"fmt"
	"os"
	"time"
)

func main() {
	fileInfo, err := os.Stat("yourfilename.ext")
	if err != nil {
		fmt.Println(err)
		return
	}

	modTime := fileInfo.ModTime()
	fmt.Println("Last modified time:", modTime.Format(time.RFC1123))
}
