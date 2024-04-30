package main

import (
	"bufio"
	"fmt"
	"net"
	"log"
)

func main() {
	listener, err := net.Listen("tcp", ":21")
	if err != nil {
		log.Fatal(err)
	}
	defer listener.Close()
	fmt.Println("FTP server started on ", listener.Addr().String())
	for {
		conn, err := listener.Accept()
		if err != nil {
			log.Print(err)
			continue
		}

		// Handle the connection in a new goroutine.
		// Handles the connection from receiving, then returns to accepting, so
		// multiple connections may be served concurrently.
		go func(c net.Conn) {
			// Note: A real FTP server for the FTP protocol here.
			fmt.Fprintf(c, "220 Welcome to the Go FTP server prototype\r\n")
			scanner := bufio.NewScanner(c)
			for scanner.Scan() {
				fmt.Println("Received command:", scanner.Text())
				fmt.Fprintf(c, "500 Unrecognized command\r\n")
			}
			c.Close()
		}(conn)
	}
}
