
package main

import (
	"fmt"
	"io/ioutil"
)

func main() {
	data, err := ioutil.ReadFile("filename.txt")
	if err != nil {
		fmt.Println("Error <extra_id_0> err)
		return
	}
	fmt.Println(string(data))
}
