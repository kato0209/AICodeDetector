
package main

import (
	"bufio"
	"fmt"
	"net"
	"os"
	"strings"
)

// FTPServer struct to maintain server state
type FTPServer struct {
	listener net.Listener
}

// StartServer starts the FTP server
func (server *FTPServer) StartServer(port string) {
	var err error
	server.listener, err = net.Listen("tcp", ":"+port)
	if err != nil {
		panic(err)
	}
	defer server.listener.Close()

	fmt.Println("FTP Server started on port", port)

	for {
		conn, err := server.listener.Accept()
		if err != nil {
			fmt.Println("Error accepting connection:", err.Error())
			continue
		}

		go server.handleConnection(conn)
	}
}

// handleConnection handles client commands
func (server *FTPServer) handleConnection(conn net.Conn) {
	defer conn.Close()

	conn.Write([]byte("220 Welcome to the Go FTP Server\r\n"))

	scanner := bufio.NewScanner(conn)
	for scanner.Scan() {
		text := scanner.Text()
		fmt.Println("Command received:", text)

		command := strings.ToUpper(strings.Fields(text)[0])

		switch command {
		case "USER":
			conn.Write([]byte("230 User logged in, proceed\r\n"))
		case "QUIT":
			conn.Write([]byte("221 Goodbye\r\n"))
			return
		default:
			conn.Write([]byte("500 Unknown command\r\n"))
		}
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading from connection:", err.Error())
	}
}

// FTPClient struct to maintain client state
type FTPClient struct {
	connection net.Conn
}

// Connect connects to the FTP server
func (client *FTPClient) Connect(server string, port string) error {
	var err error
	client.connection, err = net.Dial("tcp",