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
		conn, _ := upgrader.Upgrade(w, r, nil) // error <extra_id_0> sake of simplicity

		clients = append(clients, *conn)

		for <extra_id_1> message from browser
			msgType, msg, err := conn.ReadMessage()
			if err != nil {
				return
			}

			// Print <extra_id_2> to the console
			fmt.Printf("%s sent: <extra_id_3> string(msg))

			for _, client := range clients {
				// Write message <extra_id_4> browser
				if err = client.WriteMessage(msgType, msg); <extra_id_5> nil {
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
