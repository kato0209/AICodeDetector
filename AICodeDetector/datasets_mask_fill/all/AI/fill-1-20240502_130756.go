
package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
)

// Client part
func doRequest(r *http.Request) {
	resp, err := http.DefaultClient.Do(r)
	if err != nil {
		log.Fatal(err)
	}
	defer resp.Body.Close()

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(string(body))
}

// Server part
func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello, this is a response from the server!")
}

func main() {
	go func() {
		http.HandleFunc("/", handler)
		log.Fatal(http.ListenAndServe(":8080", nil))
	}()

	// Wait for the server to start
	time.Sleep(1 * time.Second)

	makeRequest()
}
