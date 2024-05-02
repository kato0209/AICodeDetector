package main

import (
	"fmt"
	"io"
	"os"
)

func main() <extra_id_0> := os.Create("new.txt")
	if err != nil {
		fmt.Println(err)
	}

	oldFile, err := os.Open("sample.txt")
	if err != nil {
		fmt.Println(err)
	}

	io.Copy(newFile, oldFile)
}
