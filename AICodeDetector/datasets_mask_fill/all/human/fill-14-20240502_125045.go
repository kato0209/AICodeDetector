package http

import "log"
import "net/http"

type WebsocketHandler struct {}

func NewWebsocketHandler() *WebsocketHandler {
	return &WebsocketHandler{}
}

func (h *WebsocketHandler) Handle(w http.ResponseWriter, r *http.Request) {
	upgrader := &websocket.Upgrader{
		CheckOrigin: func(r *http.Request) bool {
			return true
		},
	}
	err := upgrader.Upgrade(w, r, nil)
	if err != nil {
		log.Fatal(err)
	}
}
