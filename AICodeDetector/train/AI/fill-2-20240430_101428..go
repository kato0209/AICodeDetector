package main

import (
	"fmt"
	"log"
	"os"
	"time"
)

func wasModifiedWithin24Hours(filename string) (bool, error) {
	fileInfo, err := os.Stat(filename)
	if err != nil {
		return false, err
	}

	modifiedTime := fileInfo.ModTime()
	return time.Since(modifiedTime) <= 24*time.Hour, nil
}

func main() {
	filename := "example.txt"

	modifiedRecently, err := wasModifiedWithin24Hours(filename)
	if err!= nil {
		log.Fatalf("Error checking file modification (%v)", err)
	}

	if modifiedRecently {
		fmt.Printf("%s was modified within the last 24 hours.\n", filename)
	} else {
		fmt.Printf("%s was not modified within the last 24 hours.\n", filename)
	}
}
