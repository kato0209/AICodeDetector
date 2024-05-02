
package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
)

func downloadFileFromURL(url string, filename string) error {
	// Create the file
	out, err := os.Create(filename)
	if err != nil {
		return err
	}

	// Get the request
	resp, err := http.Get(url)
	if err != nil {
		return err
	}
	defer resp.Body.Close()

	// Check server response
	if resp.StatusCode != http.StatusOK {
		return fmt.Errorf("bad status: %s", resp.Status)
	}

	// Write the body to file
	_, err = ioutil.ReadAll(io.TeeReader(resp.Body, out))
	return err
}

func main() {
	url := "https://example.com/somefile.mp3"
	filename := "downloadedfile.mp3"

	if err := downloadFileFromURL(url, filename); err != nil {
		log.Fatal(err)
	}
}
