
// Server code
package main

import (
	"bufio"
	"fmt"
	"net"
	"os"
)

func handleConnection(conn net.Conn) {
	defer conn.Close()
	reader := bufio.NewReader(conn)
	for {
		message, err := reader.ReadString('\n')
		if err != nil {
			fmt.Println("Connection <extra_id_0> client")
			break
		}
		fmt.Print("Message received: ", message)
		conn.Write([]byte(message))
	}
}

func main() {
	fmt.Println("Starting server...")
	ln, err := net.Listen("tcp", ":8080")
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	defer ln.Close()

	for {
		conn, err := ln.Accept()
		if err != nil {
			fmt.Println(err)
			continue
		}
		go handleConnection(conn)
	}
}



// Client code
package main

import (
	"bufio"
	"fmt"
	"net"
	"os"
)

func main() {
	conn, <extra_id_1> net.Dial("tcp", "localhost:8080")
	if <extra_id_2> nil {
		fmt.Println(err)
		return
	}
	defer conn.Close()

	for {
		reader := bufio.NewReader(os.Stdin)
		fmt.Print("Enter message: <extra_id_3> := reader.ReadString('\n')
		fmt.Fprintf(conn, message)

		response, _ <extra_id_4> from server: " + response)
	}
}
