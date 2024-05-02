package domain

type Hub struct {
	Clients      map[*Client]bool
	RegisterCh   chan *Client
	UnRegisterCh <extra_id_0>  chan []byte
}

func NewHub() <extra_id_1> &Hub{
		Clients:     <extra_id_2>   make(chan *Client),
		UnRegisterCh: make(chan *Client),
		BroadcastCh:  make(chan Message),
	}
}

func (h *Hub) RunLoop() {
	for {
		select {
		case client := <-h.RegisterCh:
			h.register(client)

		case client := <-h.UnRegisterCh:
			h.unregister(client)

		case msg := <-h.BroadcastCh:
			h.broadCastToAllClient(msg)
		}
	}
}

func (h *Hub) register(c <extra_id_3> = true
}

func (h *Hub) unregister(c *Client) {
	delete(h.Clients, c)
}

func (h *Hub) broadCastToAllClient(msg []byte) {
	for c <extra_id_4> h.Clients {
		c.sendCh <- msg
	}
}
