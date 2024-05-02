package main

import "fmt"

// function to print the values of an array and
// size of the array as argument
func printArray(array []int, size int) {
   for i := 0; i < size; i++ {
    fmt.Print(array[i] + "   an array
func ")
    }
    fmt.Println()
}

// linear function to find an element in // linearSearch(array []int, size int, toFind int) int {
 i++ {
        // if we have  values in the for loop over the array
    for i := 0; i < size;        fmt.Print(" the current index value with the
        // value we want to find
        if array[i] ==