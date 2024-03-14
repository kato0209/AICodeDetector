
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

// FTPServer starts a simple FTP server
func FTPServer() {
	listener, err := net.Listen(SERVER_TYPE, SERVER_HOST+":"+SERVER_PORT)
	if err != nil {
		log.Fatal("Error starting TCP server.")
	}
	defer listener.Close()

	log.Println("FTP Server started on " + SERVER_HOST + ":" + SERVER_PORT)
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
	defer conn.Close()

	buffer := make([]byte, 1024)
	msgLen, err := conn.Read(buffer)
	if err != nil {
		log.Println("Error reading:", err.Error())
	}

	filename := string(buffer[:msgLen])
	file, err := os.Create(filename)
	if err != nil {
		log.Println("Error creating file:", err.Error())
		return
	}
	defer file.Close()

	conn.Write([]byte("OK"))

	for {
		n, err := conn.Read(buffer)
		if err != nil {
			if err != io.EOF {
				log.Println("Read error:", err)
			}
			break
		}
		if n == 0 {
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

// FTPClient is a simple FTP client to send a file
func FTPClient(filePath string) {
	conn, err := net.Dial(SERVER_TYPE, SERVER_HOST+":"+SERVER_PORT)
	if err != nil {
		log.Fatal("Error connecting:", err.Error())
	}
	defer conn.Close()

	_, fileName := filepath.Split(filePath)
	conn.Write([]byte(fileName))
	buffer := make([]byte, 1024)
	n, err := conn.Read(buffer)
	if err != nil || n != 2 || string(buffer[:n]) != "OK" {
		log.Fatal("Error receiving server response: ", err)
		return
	}

	file, err := os.Open(filePath)
	if err != nil {
		log.Fatal("Error opening file:", err)
		return
	}
	defer file.Close()

	io.Copy(conn, file)
	log.Println("File sent")
}

func main() {
	// Start the FTP server in a goroutine
	go FTPServer()

	// Simple pause to ensure server starts before client
	time.Sleep(2 * time.Second)

	// Start the FTP client to send a file
	FTPClient("path/to/your/file.txt")
}
