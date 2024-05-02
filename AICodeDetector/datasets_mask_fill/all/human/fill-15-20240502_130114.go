package main

import (
    "fmt"
    "os"
     "log"
)

func main() {
   entries, err := Read(os.Args[1:])   if err != nil {       log.Fatal(err)
   }
 
    for _, e := range entries {
           PrintContents(e)    }
}
