
package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
)

// Server
func startServer() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, "Hello from the server!")
	})

	log.Fatal(http.ListenAndServe(":8080", nil))
}

// Client
func sendRequest() {
	resp, err := http.Get("http://localhost:8080")
	if err != nil {
		log.Fatal(err)
	}
	defer resp.Body.Close()

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Printf("%s\n", body)
}

func main() {
	go startServer()

	// Wait for the server to start
	time.Sleep(1 * time.Second)

	sendRequest()
}
