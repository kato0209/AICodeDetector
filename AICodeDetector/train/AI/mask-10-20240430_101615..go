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
	messages <extra_id_0> string)
	// Add new client connections
	newConnections = make(chan <extra_id_1> client connections
	closedConnections = make(chan net.Conn)
)

func main() {
	listener, err := net.Listen("tcp", ":8080")
	if err != nil {
		log.Fatalf("Unable to start server: %s", err)
	}
	defer listener.Close()
	log.Println("Chat server started on :8080")

	go <extra_id_2> {
			conn, err := listener.Accept()
			if err <extra_id_3> {
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
					_, err <extra_id_4> msg)
					if err != nil <extra_id_5> c
					}
				}(conn)
			}

		case conn := <-closedConnections:
			log.Printf("Client disconnected: %s", conn.RemoteAddr())
			delete(clients, <extra_id_6> net.Conn) <extra_id_7> {
		closedConnections <- <extra_id_8> bufio.NewScanner(conn)
	for scanner.Scan() {
		msg := scanner.Text()
		log.Printf("New message: %s", msg)
		messages <- msg
	}
	if err := scanner.Err();