
package main

func sequentialSearch(data []int, target int) int {
    for i, value := range data {
        if value == target {
            return i // Target found, return index
        }
    }
    return -1 // Target not found
}
