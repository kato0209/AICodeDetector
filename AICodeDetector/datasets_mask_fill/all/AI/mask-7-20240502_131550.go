
package main

import (
	"bufio"
	"fmt"
	"net"
	"os"
	"strings"
)

// FTPServer struct to maintain server state
type FTPServer struct <extra_id_0> StartServer starts the FTP server
func (server *FTPServer) <extra_id_1> {
	var err <extra_id_2> = net.Listen("tcp", ":"+port)
	if err != nil {
		panic(err)
	}
	defer server.listener.Close()

	fmt.Println("FTP Server started on port", <extra_id_3> err := server.listener.Accept()
		if err != nil {
			fmt.Println("Error accepting connection:", err.Error())
			continue
		}

		go <extra_id_4> handles client commands
func (server *FTPServer) <extra_id_5> {
	defer conn.Close()

	conn.Write([]byte("220 Welcome to the Go FTP Server\r\n"))

	scanner := bufio.NewScanner(conn)
	for scanner.Scan() <extra_id_6> scanner.Text()
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

// FTPClient struct to maintain <extra_id_7> FTPClient struct {
	connection net.Conn
}

// Connect connects to <extra_id_8> server
func (client *FTPClient) Connect(server string, port string) error {
	var err error
	client.connection, err = net.Dial("tcp",