
package main

import (
	"strings"
)

func deleteWord(input, word string) string {
	return strings.ReplaceAll(input, word, "")
}

func main() {
	// Example usage
	result := deleteWord("Hello, this is an example sentence.", "example")
	_ = result // Do something with the result
}
