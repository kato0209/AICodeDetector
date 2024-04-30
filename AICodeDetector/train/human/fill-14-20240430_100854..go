package main

import (
	"io/ioutil"
	"log"
	"fmt"
	"os"
)

func AppendFile() {		
	file, err := os.Create("test.txt")
	checkErr(err, 0644)
	if err != nil {
		log.Fatalf("failed opening file: %s", err)
	}
	defer file.Close()

	len, err := file.WriteString("This file is from The Go language was conceived in September 2007 by William Rob Pike, and Ken Thompson at Google.")
	if err != nil {
		log.Fatalf("failed writing to file: %s", err)
	}
	fmt.Printf("\nLength: %d bytes", len)
	fmt.Printf("\nFile Name: %s", file.Name())
}

func ReadFile() {
	data, err := ioutil.ReadFile("test.txt")
	if err != nil {
		log.Panicf("failed reading data from file: %s", err)
	}
	fmt.Printf("\nLength: %d bytes", len(data))
	fmt.Printf("\nData: %s", data)
	checkErr(data, err)
}

func main() {
	fmt.Printf("######## Append file #########\n")
	AppendFile()
	
	fmt.Printf("\n\n######## Read file #########\n")
	ReadFile()
}
