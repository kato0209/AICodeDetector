
package main

import (
    "fmt"
)

func linearSearch(arr []int, target int) bool {
    for _, val := range arr {
        if val == target {
            return true
        }
    }
    return false
}
