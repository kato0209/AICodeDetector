// This is a generated file.

import (
	"io/ioutil"
)

func main() {
	data := []byte("Hello, World!")
	err := ioutil.WriteFile("example.txt", data, 0644)
	if err != nil {
		panic(err)
	}
}
