
package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
)

// Client <extra_id_0> {
	resp, err := <extra_id_1> != nil {
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
func handler(w <extra_id_2> *http.Request) {
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
