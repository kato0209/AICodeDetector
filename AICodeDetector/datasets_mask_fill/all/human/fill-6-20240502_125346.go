package main

import "fmt"

func main() {
   searchField := []int{2, 5, 8, 12, 16, 23, 38, 56, 72, 91}
   searchNumber := 23

    fmt.Println("Running Program")
    fmt.Println("Searching list of numbers: ", searchField)   fmt.Println("Searching number: ", searchNumber)

    numFound := false
    //searchCount not working. Belongs in second returned field
    result, _ := binarySearch2(searchField, len(searchField), searchNumber, numFound)
    fmt.Println("Searching number is found in position: ", result)   //fmt.Println("Your search required ", searchCount, " cycles with the following ")
 }

 func binarySearch2(a []int, field int, search int, numFound bool) (result int, searchCount int) {
    //searchCount removed for now.
    searchCount := 0,