
package main

import (
	"bufio"
	"fmt"
	"net"
	"os"
	"strings"
)

// FTPServer struct to hold server information
type FTPServer struct {
	Address string // Address to bind the server to
}

// Start starts the FTP server
func (s *FTPServer) Start() {
	ln, err := net.Listen("tcp", s.Address)
	if err != nil {
		fmt.Println("Error starting server:", err)
		return
	}
	defer ln.Close()
	fmt.Println("FTP Server started on", s.Address)

	for {
		conn, err := ln.Accept()
		if err != nil {
			fmt.Println("Error accepting connection:", err)
			continue
		}
		go s.handleConnection(conn)
	}
}

// handleConnection handles individual client connections
func (s *FTPServer) handleConnection(conn net.Conn) {
	defer conn.Close()
	conn.Write([]byte("220 Welcome to the Go FTP Server\r\n"))

	scanner := bufio.NewScanner(conn)
	for scanner.Scan() {
		text := scanner.Text()
		cmd := strings.ToUpper(strings.TrimSpace(text))
		switch cmd {
		case "QUIT":
			conn.Write([]byte("221 Goodbye!\r\n"))
			return
		default:
			conn.Write([]byte("500 Unknown command\r\n"))
		}
	}
}

// FTPClient struct to hold client information
type FTPClient struct {
	ServerAddress string // Address of the FTP server to connect to
}

// Connect connects to the FTP server
func (c *FTPClient) Connect() {
	conn, err := net.Dial("tcp", c.ServerAddress)
	if err != nil {
		fmt.Println("Error connecting to server:", err)
		return
	}
	defer conn.Close()

	scanner := bufio.NewScanner(conn)
	for scanner.Scan() {
		fmt.Println("Server:", scanner.Text())
	}

	fmt.Println("Connection to server closed.")
}

func main() {
	// Start FTP server
	server := FTPServer{Address: "localhost:2121"}
	go server.Start()

	// Give the server a moment to start
	time.Sleep(1 * time.Second)

	// Start FTP client
	client := FTPClient{ServerAddress: "localhost:2121"}
	client.Connect()
}
