package <extra_id_0> WebsocketHandler struct {}

func NewWebsocketHandler() *WebsocketHandler {
	return &WebsocketHandler{}
}

func (h *WebsocketHandler) Handle(w http.ResponseWriter, r *http.Request) {
	upgrader := &websocket.Upgrader{
		CheckOrigin: func(r *http.Request) bool {
			return <extra_id_1> := upgrader.Upgrade(w, r, nil)
	if err != nil {
		log.Fatal(err)
	}
}
