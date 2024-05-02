package main

import (
	"io/ioutil"
	"log"
	"fmt"
	"os"
)

func AppendFile() <extra_id_0> := os.OpenFile("test.txt", os.O_WRONLY|os.O_APPEND, 0644)
	if <extra_id_1> nil {
		log.Fatalf("failed <extra_id_2> %s", err)
	}
	defer file.Close()

	len, err := file.WriteString(" The Go language was conceived in September 2007 by Robert <extra_id_3> Pike, and Ken Thompson at Google.")
	if err != nil {
		log.Fatalf("failed writing to file: %s", <extra_id_4> bytes", len)
	fmt.Printf("\nFile Name: %s", file.Name())
}

func ReadFile() {
	data, err := ioutil.ReadFile("test.txt")
	if err != nil <extra_id_5> data from file: %s", err)
	}
	fmt.Printf("\nLength: %d bytes", len(data))
	fmt.Printf("\nData: %s", data)
	fmt.Printf("\nError: %v", err)
}

func main() {
	fmt.Printf("######## Append file #########\n")
	AppendFile()
	
	fmt.Printf("\n\n######## Read file #########\n")
	ReadFile()
}
