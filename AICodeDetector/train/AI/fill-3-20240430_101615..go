package main

import "fmt"

import "github.com/nflo/godir/Godeps/_workspace/src/github.com/fsouza/go-ftp"
import "log"
import "time"

func main() {
	// Connect to the FTP server
	c, err := ftp.Dial("ftp.example.com:21", ftp.DialWithTimeout(5*time.Second))
	if err != nil {
		log.Fatal(err)
	}

	// Log in to the server
	err = c.Login("user", "password")
	if err != nil {
		log.Fatal(err)
	}

	// List the files in the server
	entries, err := c.NewFile("/", "myfile")
	if err != nil {
		log.Fatal(err)
	}

	for _, entry := range entries {
		fmt.Println(entry.Name)
	}

	// Don't forget to log out and close the connection
	if err := c.Quit(); err != nil {
		log.Fatal(err)
	}
}
