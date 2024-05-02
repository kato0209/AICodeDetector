lang
// server.go
package <extra_id_0> handleConnection(conn net.Conn) {
	defer <extra_id_1> err := bufio.NewReader(conn).ReadString('\n')
		if err != nil {
			log.Printf("Error reading from client: <extra_id_2> Received: %s", message)
		conn.Write([]byte("Message received: " + message))
	}
}

func main() {
	listener, err := net.Listen("tcp", ":8080")
	if err != nil {
		log.Fatalf("Failed to listen on port 8080: %v", <extra_id_3> listening on port 8080")

	for {
		conn, err := listener.Accept()
		if err != nil {
			log.Printf("Failed to accept connection: %v", <extra_id_4> client.go
package <extra_id_5> main() {
	conn, err := net.Dial("tcp", "localhost:8080")
	if err != nil {
		fmt.Println(err)
		return
	}
	defer conn.Close()

	for {
		reader := <extra_id_6> ")
		text, _ := reader.ReadString('\n')
		fmt.Fprintf(conn, text+"\n")

		message, _ := bufio.NewReader(conn).ReadString('\n')
		fmt.Print("Message from server: " + message)
	}
}
