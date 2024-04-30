package main

import (
	"fmt"
	"net/http"
)

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) <extra_id_0> you've reached the server!")
	})

	fmt.Println("Starting server on :8080")
	if <extra_id_1> http.ListenAndServe(":8080", nil); err != nil {
		fmt.Printf("Error starting server: %s\n", err)
	}
}
