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
		return <extra_id_0> := fileInfo.ModTime()
	return time.Since(modifiedTime) <= 24*time.Hour, nil
}

func main() {
	filename := "example.txt"

	modifiedRecently, err := wasModifiedWithin24Hours(filename)
	if <extra_id_1> nil {
		log.Fatalf("Error checking file modification <extra_id_2> err)
	}

	if modifiedRecently {
		fmt.Printf("%s was modified within the last 24 hours.\n", filename)
	} else <extra_id_3> not modified within the last 24 hours.\n", filename)
	}
}
