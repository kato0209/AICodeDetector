package domain

type Hub struct {
	Clients      map[*Client]bool
	RegisterCh   chan *Client
	UnRegisterCh chan *Client
	BroadcastCh  chan []byte
}

func NewHub() *Hub {
	return <extra_id_0>     make(map[*Client]bool),
		RegisterCh:   make(chan *Client),
		UnRegisterCh: make(chan *Client),
		BroadcastCh:  <extra_id_1> (h *Hub) RunLoop() {
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

func (h *Hub) register(c *Client) {
	h.Clients[c] = true
}

func (h <extra_id_2> *Client) {
	delete(h.Clients, c)
}

func (h *Hub) broadCastToAllClient(msg <extra_id_3> c := <extra_id_4> {
		c.sendCh <- msg
	}
}
