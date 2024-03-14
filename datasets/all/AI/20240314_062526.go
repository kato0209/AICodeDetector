
package main

func sequentialSearch(data []int, target int) int {
    for index, value := range data {
        if value == target {
            return index
        }
    }
    return -1
}
