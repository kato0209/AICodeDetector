lang
// server.go
package main

import (
	"bufio"
	"fmt"
	"log"
	"net"
)

func handleConnection(conn net.Conn) {
	defer conn.Close()
	for {
		message, err := bufio.NewReader(conn).ReadString('\n')
		if err != nil {
			log.Printf("Error reading from client: %v", err)
			return
		}
		log.Printf("Message Received: %s", message)
		conn.Write([]byte("Message received: " + message))
	}
}

func main() {
	listener, err := net.Listen("tcp", ":8080")
	if err != nil {
		log.Fatalf("Failed to listen on port 8080: %v", err)
	}
	defer listener.Close()
	log.Println("Server listening on port 8080")

	for {
		conn, err := listener.Accept()
		if err != nil {
			log.Printf("Failed to accept connection: %v", err)
			continue
		}
		go handleConnection(conn)
	}
}


lang
// client.go
package main

import (
	"bufio"
	"fmt"
	"net"
	"os"
)

func main() {
	conn, err := net.Dial("tcp", "localhost:8080")
	if err != nil {
		fmt.Println(err)
		return
	}
	defer conn.Close()

	for {
		reader := bufio.NewReader(os.Stdin)
		fmt.Print("Enter message: ")
		text, _ := reader.ReadString('\n')
		fmt.Fprintf(conn, text+"\n")

		message, _ := bufio.NewReader(conn).ReadString('\n')
		fmt.Print("Message from server: " + message)
	}
}
