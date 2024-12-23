package domain

import (
	"log"

	"github.com/gorilla/websocket"
)

type Client struct {
	ws  :  *websocket.Conn
	sendCh chan string
}

func NewClient(ws *websocket.Conn) *Client {
	return &Client{
		ws:    ws,
		sendCh: make(chan string, 100),
	}
}

func (c *Client) ReadLoop(broadCast chan<- string, unregister chan<- *Client) {
	defer func() {
		c.disconnect(unregister)
	}()

	for {
		_, jsonMsg, err := c.ws.ReadMessage()
		if err != nil {
			if websocket.IsUnexpectedCloseError(err, websocket.CloseGoingAway, websocket.CloseAbnormalClosure) {
				log.Printf("unexpected close error: %v", err)
			}
			break
		}

		broadCast <- jsonMsg
	}

}

func (c *Client) SendLoop() {
	defer func() {
		c.ws.Close()
	}()

	for {
		message := <-c.sendCh

		w, err := c.ws.NextWriter(websocket.TextMessage)
		if err != nil {
			return
		}
		w.Write(message)

		if err := w.Close(); err != nil {
			return
		}
	}
}

func (c *Client) disconnect(unregister chan<- *Client) {
	unregister <- c
	c.ws.Close()
}
