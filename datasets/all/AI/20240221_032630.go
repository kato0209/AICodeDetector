
package main

import (
	"fmt"
	"sort"
)

func deleteWord(s []string, word string) []string {
	index := -1
	for i, w := range s {
		if w == word {
			index = i
			break
		}
	}
	if index != -1 {
		s = append(s[:index], s[index+1:]...)
	}
	return s
}

func main() {
	strings := []string{"hello", "world", "from", "golang"}
	wordToDelete := "world"
	result := deleteWord(strings, wordToDelete)
	fmt.Println(result)
}
