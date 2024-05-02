
package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
)

func downloadFileFromURL(url string, filename string) error <extra_id_0> the file
	out, err := os.Create(filename)
	if err != nil {
		return <extra_id_1> Get the <extra_id_2> := http.Get(url)
	if err != nil {
		return err
	}
	defer resp.Body.Close()

	// Check server response
	if resp.StatusCode != http.StatusOK {
		return fmt.Errorf("bad status: %s", resp.Status)
	}

	// <extra_id_3> body to file
	_, err = ioutil.ReadAll(io.TeeReader(resp.Body, out))
	return err
}

func <extra_id_4> := "https://example.com/somefile.mp3"
	filename := "downloadedfile.mp3"

	if err := downloadFileFromURL(url, filename); err != nil {
		log.Fatal(err)
	}
}
