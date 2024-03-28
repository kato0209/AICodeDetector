
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

// Connect connects to an FTP server
func (client *FTPClient) Connect(server string, port string) error {
	var err error
	client.connection, err = net.Dial("tcp", server+":"+port)
	if err != nil {
		return err
	}
	return nil
}

// SendCommand sends commands to the FTP server
func (client *FTPClient) SendCommand(command string) (string, error) {
	_, err := client.connection.Write([]byte(command + "\r\n"))
	if err != nil {
		return "", err
	}

	response, err := bufio.NewReader(client.connection).ReadString('\n')
	if err != nil {
		return "", err
	}

	return response, nil
}

// Close closes the client connection
func (client *FTPClient) Close() error {
	if client.connection != nil {
		err := client.connection.Close()
		if err != nil {
			return err
		}
	}
	return nil
}

func main() {
	// Start server in go routine
	go func() {
		server := FTPServer{}
		server.StartServer("21")
	}()

	// Simple pause to wait for the server to start
	// In real scenarios, ensure the server is started before the client attempts to connect.
	select {}

	// // Example client usage
	// client := FTPClient{}
	// err := client.Connect("localhost", "21")
	// if err != nil {
	// 	fmt.Println("Error connecting to server:", err)
	// 	return
	// }
	// defer client.Close()

	// response, err := client.SendCommand("USER anonymous")
	// if err != nil {
	// 	fmt.Println("Error sending command:", err)
	// 	return
	// }
	// fmt.Println("Response:", response)

	// response, err = client.SendCommand("QUIT")
	// if err != nil {
	// 	fmt.Println("Error sending command:", err)
	// 	return
	// }
	// fmt.Println("Response:", response)
}
