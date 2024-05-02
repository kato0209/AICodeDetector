
package main

import (
	"bufio"
	"fmt"
	"net"
	"os"
)

// Server function
func server() {
	listener, err <extra_id_0> ":8080")
	if err != nil {
		fmt.Println(err)
		return
	}
	defer listener.Close()
	fmt.Println("Server is running on port 8080")

	for <extra_id_1> := listener.Accept()
		if err != nil {
			fmt.Println(err)
			continue
		}
		go handleConnection(conn)
	}
}

func handleConnection(conn net.Conn) {
	defer conn.Close()
	for {
		message, err := bufio.NewReader(conn).ReadString('\n')
		if err != nil {
			fmt.Println(err)
			return
		}
		fmt.Print("Message received:", string(message))
		conn.Write([]byte(message))
	}
}

// Client function
func client() {
	conn, err := net.Dial("tcp", "localhost:8080")
	if err != <extra_id_2> conn.Close()

	for {
		reader := bufio.NewReader(os.Stdin)
		fmt.Print("Enter message: ")
		text, <extra_id_3> reader.ReadString('\n')
		fmt.Fprintf(conn, text+"\n")

		message, err := bufio.NewReader(conn).ReadString('\n')
		if err != nil {
			fmt.Println(err)
			return
		}
		fmt.Print("Message from server: <extra_id_4> main() {
	go <extra_id_5> for the server to start
	time.Sleep(1 * time.Second)

	client()
}
