package main

import (
	"fmt"
	"net/http"

	"github.com/gorilla/websocket"
)

var upgrader = websocket.Upgrader{
	ReadBufferSize:  1024,
	WriteBufferSize: 1024,
}

var clients []websocket.Conn

func main() {
	http.HandleFunc("/echo", func(w http.ResponseWriter, r *http.Request) {
		conn, _ := upgrader.Upgrade(w, r, nil) // error for sake of simplicity

		clients = append(clients, *conn)

		for {
			// Get message from browser
			msgType, msg, err := conn.ReadMessage()
			if err != nil {
				return
			}

			// Print message sent to the console
			fmt.Printf("%s sent: %s\n", msgType, string(msg))

			for _, client := range clients {
				// Write message to browser
				if err = client.WriteMessage(msgType, msg); err!= nil {
					return
				}
			}

		}
	})

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		http.ServeFile(w, r, "index.html")
	})

	http.ListenAndServe(":8080", nil)
}
