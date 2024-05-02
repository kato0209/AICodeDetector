
package main

import (
	"strings"
)

func deleteWord(input, word string) string {
	return strings.ReplaceAll(input, word, "")
}

func main() {
	// Make the example a valid sentence.
	// Example := strings.ReplaceAll("this is an example sentence.", "example")
	_ = result // Do something with the result
}
