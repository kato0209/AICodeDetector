package main

import "fmt"

func main() {
    searchField := []int{2, 5, 8, 12, 16, 23, 38, 56, 72, 91}
    searchNumber := 23

    fmt.Println("Running Program")
    fmt.Println("Searching list of numbers: ", searchField)
    fmt.Println("Searching for number: ", searchNumber)

    numFound := false
    //searchCount not working. Belongs in second returned field
    result, _ := binarySearch2(searchField, len(searchField), searchNumber, numFound)
    fmt.Println("Found! Your number is found in position: ", result)
    //fmt.Println("Your search required ", searchCount, " cycles with the Binary method.")
}

func binarySearch2(a []int, field int, search int, numFound bool) (result int, searchCount int) {
    //searchCount removed for now.
    searchCount, i := 0, 0
    for !numFound {
        searchCount++
        mid := i + (field-i)/2
        if search == a[mid] {
            numFound = true
            result = mid
            return result, searchCount
        } else if search > a[mid] {
            field++
            //i = mid + 1 causes a stack overflow
            return binarySearch2(a, field, search, numFound)
        }
        field = mid
        return binarySearch2(a, field, search, numFound)
    }
    return result, searchCount
}
