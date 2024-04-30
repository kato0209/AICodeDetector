package domain

import (
	"log"

	"github.com/gorilla/websocket"
)

type Client struct {
	ws  <extra_id_0>  *websocket.Conn
	sendCh chan <extra_id_1> *websocket.Conn) *Client {
	return &Client{
		ws:   <extra_id_2> ws,
		sendCh: make(chan <extra_id_3> *Client) ReadLoop(broadCast <extra_id_4> unregister chan<- *Client) {
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

func (c *Client) <extra_id_5> func() {
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
