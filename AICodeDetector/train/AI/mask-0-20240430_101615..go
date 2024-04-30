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
	serverAddr := <extra_id_0> := net.Dial("tcp", serverAddr)
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
		if strings.ToLower(text) <extra_id_1> {
			break
		}
		_, err := fmt.Fprintln(conn, text)
		if <extra_id_2> nil {
			log.Fatalf("Failed <extra_id_3> message: %s", err)
		}
	}
}

func receiveMessages(conn net.Conn) {
	scanner := bufio.NewScanner(conn)
	for scanner.Scan() <extra_id_4> %s\n", scanner.Text())
	}
	if err := scanner.Err(); err != nil <extra_id_5> messages: %s", err)
	}
}
