package main

import (
	"bufio"
	"fmt"
	"net"
	"log"
)

func main() {
	listener, err := net.Listen("tcp", ":21")
	if err != nil {
		log.Fatal(err)
	}
	defer listener.Close()
	fmt.Println("FTP server started on <extra_id_0> {
		conn, <extra_id_1> listener.Accept()
		if err != nil {
			log.Print(err)
			continue
		}

		// Handle the connection in a new goroutine.
		// <extra_id_2> then returns to accepting, <extra_id_3> multiple connections may be served concurrently.
		go func(c net.Conn) {
			// Note: A real FTP server <extra_id_4> the FTP protocol here.
			fmt.Fprintf(c, "220 Welcome to the Go FTP server prototype\r\n")
			scanner := bufio.NewScanner(c)
			for scanner.Scan() {
				fmt.Println("Received command:", scanner.Text())
				fmt.Fprintf(c, "500 Unrecognized command\r\n")
			}
			c.Close()
		}(conn)
	}
}
