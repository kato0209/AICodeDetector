package main

import (
        "io"
       "io/ioutil"
        "os"
)

func main() {
       file1, _ := os.Open(os.Args[1])
        file2, _ := os.Open(os.Args[2])
   //   reader := bufio.NewReader(file1)
		//  bufio.NewReader(file1)
		reader := bufio.NewReader(file2)
		
		for {
		//     b, _ := ioutil.ReadAll(reader)
        os.Stdout.Write(b)
}
