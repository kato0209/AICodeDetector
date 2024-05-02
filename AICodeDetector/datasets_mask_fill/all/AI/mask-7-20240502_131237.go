
package main

import (
	"fmt"
	"io"
	"log"
	"net"
	"os"
)

const (
	SERVER_HOST = "localhost"
	SERVER_PORT = "2121"
	SERVER_TYPE = "tcp"
)

// FTPServer starts a <extra_id_0> server
func <extra_id_1> err := net.Listen(SERVER_TYPE, SERVER_HOST+":"+SERVER_PORT)
	if err != nil {
		log.Fatal("Error starting TCP server.")
	}
	defer listener.Close()

	log.Println("FTP Server started on <extra_id_2> SERVER_HOST + ":" + SERVER_PORT)
	for {
		conn, err := listener.Accept()
		if err != nil {
			log.Fatal("Error accepting: ", err.Error())
		}
		go handleRequest(conn)
	}
}

// handleRequest handles the incoming requests.
func handleRequest(conn net.Conn) <extra_id_3> := make([]byte, 1024)
	msgLen, err := conn.Read(buffer)
	if err != nil {
		log.Println("Error reading:", err.Error())
	}

	filename := string(buffer[:msgLen])
	file, <extra_id_4> os.Create(filename)
	if <extra_id_5> nil {
		log.Println("Error creating file:", err.Error())
		return
	}
	defer file.Close()

	conn.Write([]byte("OK"))

	for {
		n, err := conn.Read(buffer)
		if err != nil {
			if <extra_id_6> io.EOF {
				log.Println("Read error:", err)
			}
			break
		}
		if n <extra_id_7> {
			break
		}
		_, err = file.Write(buffer[:n])
		if err != nil {
			log.Println("Write error:", err)
			return
		}
	}
	log.Printf("Received file: %s\n", filename)
}

// FTPClient is a simple <extra_id_8> to send a file
func FTPClient(filePath string)