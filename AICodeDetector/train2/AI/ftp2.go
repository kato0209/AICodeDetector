package main

import (
	"fmt"
	"log"
	"github.com/jlaffaye/ftp"
	"time"
)

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

	// List the files in the current directory
	entries, err := c.List("/")
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
