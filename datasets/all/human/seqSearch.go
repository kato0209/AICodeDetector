package main

import "fmt"

// function to print the array with array and
// size of the array as argument
func printArray(array []int, size int) {
    for i := 0; i < size; i++ {
        fmt.Print(array[i], " ")
    }
    fmt.Println()
}

// linear function to find an element in the array
func linearSearch(array []int, size int, toFind int) int {
    // running for loop over the array
    for i := 0; i < size; i++ {
        //Comparing the current index value with the
        // value we want to find
        if array[i] == toFind {
            return i
        }
    }

    // returning -1 if value not present in the array
    return -1
}

func main() {
    // declaring and initializing the
    // array using the shorthand method
    array := []int{10, 5, 3, 7, 6, 12}

    // declaring and initializing the
    // variable using the var keyword
    var toSearch int
    toSearch = 3

    fmt.Println("Golang program to find an element in an array using linear search.")
    fmt.Print("array:")
    printArray(array, 6)
    // linear search function passing array and
    // variable as a parameter
    index := linearSearch(array, 6, toSearch)

    if index == -1 {
        fmt.Println(toSearch, "is not present in the array.")
    } else {
        fmt.Println(toSearch, "is present at index 2  in the array.")
    }
}
