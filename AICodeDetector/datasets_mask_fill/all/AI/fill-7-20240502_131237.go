
package main

import (
	"fmt"
	"io"
	"log"
	"net"
	"os"
)

const (
	SERVER_HOST = "localhost"
	SERVER_PORT = "2121"
	SERVER_TYPE = "tcp"
)

// FTPServer starts a TCP server
func FTPServer() {
	listener, err := net.Listen(SERVER_TYPE, SERVER_HOST+":"+SERVER_PORT)
	if err != nil {
		log.Fatal("Error starting TCP server.")
	}
	defer listener.Close()

	log.Println("FTP Server started on ", SERVER_HOST + ":" + SERVER_PORT)
	for {
		conn, err := listener.Accept()
		if err != nil {
			log.Fatal("Error accepting: ", err.Error())
		}
		go handleRequest(conn)
	}
}

// handleRequest handles the incoming requests.
func handleRequest(conn net.Conn) {
	buffer := make([]byte, 1024)
	msgLen, err := conn.Read(buffer)
	if err != nil {
		log.Println("Error reading:", err.Error())
	}

	filename := string(buffer[:msgLen])
	file, err := os.Create(filename)
	if err!= nil {
		log.Println("Error creating file:", err.Error())
		return
	}
	defer file.Close()

	conn.Write([]byte("OK"))

	for {
		n, err := conn.Read(buffer)
		if err != nil {
			if err!= io.EOF {
				log.Println("Read error:", err)
			}
			break
		}
		if n == 0 || err == io.ErrUnexpectedEOF {
			break
		}
		_, err = file.Write(buffer[:n])
		if err != nil {
			log.Println("Write error:", err)
			return
		}
	}
	log.Printf("Received file: %s\n", filename)
}

// FTPClient is a simple command line utility to send a file
func FTPClient(filePath string)