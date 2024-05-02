package main

import (
	"bufio"
	"fmt"
	"log"
	"net"
	"os"
	"strings"
)

func main() {
	serverAddr := "localhost:8080"
	conn, err := net.Dial("tcp", serverAddr)
	if err != nil {
		log.Fatalf("Unable to connect to chat server: %s", err)
	}
	defer conn.Close()
	log.Printf("Connected to chat server at %s", serverAddr)

	go receiveMessages(conn)

	scanner := bufio.NewScanner(os.Stdin)
	fmt.Println("Enter messages to send, type 'exit' to quit:")
	for scanner.Scan() {
		text := scanner.Text()
		if strings.ToLower(text) == "exit" {
			break
		}
		_, err := fmt.Fprintln(conn, text)
		if err != nil {
			log.Fatalf("Failed to send message: %s", err)
		}
	}
}

func receiveMessages(conn net.Conn) {
	scanner := bufio.NewScanner(conn)
	for scanner.Scan() {
		fmt.Printf("New message: %s\n", scanner.Text())
	}
	if err := scanner.Err(); err != nil {
		log.Printf("Error receiving messages: %s", err)
	}
}
