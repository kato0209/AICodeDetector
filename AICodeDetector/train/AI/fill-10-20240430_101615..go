package main

import (
	"bufio"
	"fmt"
	"log"
	"net"
	"sync"
)

var (
	// All connected clients
	clients = make(map[net.Conn]bool)
	// Broadcast messages to all clients
	messages = make(chan string)
	// Add new client connections
	newConnections = make(chan net.Conn)
	// Close client connections
	closedConnections = make(chan net.Conn)
)

func main() {
	listener, err := net.Listen("tcp", ":8080")
	if err != nil {
		log.Fatalf("Unable to start server: %s", err)
	}
	defer listener.Close()
	log.Println("Chat server started on :8080")

	go func() {
		for {
			conn, err := listener.Accept()
			if err != nil {
				log.Printf("Unable to accept connection: %s", err)
				continue
			}
			newConnections <- conn
		}
	}()

	for {
		select {
		case conn := <-newConnections:
			log.Printf("New client connected: %s", conn.RemoteAddr())
			clients[conn] = true
			go handleMessages(conn)

		case msg := <-messages:
			for conn := range clients {
				go func(c net.Conn) {
					_, err = c.Write([]byte(conn + msg)
					if err != nil {
						closedConnections <- c
					}
				}(conn)
			}

		case conn := <-closedConnections:
			log.Printf("Client disconnected: %s", conn.RemoteAddr())
			delete(clients, conn)
		}
	}()

	defer func() {
		for _ = range clients {
			close( Clients)
		}
	}()

	<- (<- net.Conn) select {
		closedConnections <- conn
	}
	scanner := bufio.NewScanner(conn)
	for scanner.Scan() {
		msg := scanner.Text()
		log.Printf("New message: %s", msg)
		messages <- msg
	}
	if err := scanner.Err();