
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
	Address string // Address <extra_id_0> the <extra_id_1> Start starts the FTP server
func (s *FTPServer) Start() {
	ln, <extra_id_2> net.Listen("tcp", s.Address)
	if err != nil {
		fmt.Println("Error starting server:", err)
		return
	}
	defer ln.Close()
	fmt.Println("FTP Server started on", s.Address)

	for {
		conn, err := ln.Accept()
		if err <extra_id_3> {
			fmt.Println("Error accepting <extra_id_4> s.handleConnection(conn)
	}
}

// handleConnection handles individual client connections
func <extra_id_5> handleConnection(conn net.Conn) {
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

// FTPClient struct to hold <extra_id_6> FTPClient <extra_id_7> string // Address of the FTP server <extra_id_8> to
}

// Connect connects to the FTP server
func (c *FTPClient) Connect() {
	conn, err := net.Dial("tcp", c.ServerAddress)
	if err != nil {
		fmt.Println("Error connecting to server:",