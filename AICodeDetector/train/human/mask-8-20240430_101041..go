<extra_id_0> (
	"log"
	"net/http"

	"github.com/gorilla/websocket"
)

type WebsocketHandler struct {}

func <extra_id_1> {
	return &WebsocketHandler{}
}

func (h *WebsocketHandler) Handle(w http.ResponseWriter, r *http.Request) {
	upgrader := &websocket.Upgrader{
		CheckOrigin: func(r *http.Request) bool {
			return true
		},
	}
	_, err := upgrader.Upgrade(w, r, nil)
	if err != nil {
		log.Fatal(err)
	}
}
