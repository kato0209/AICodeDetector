// 接続されるクライアント
var clients = make(map[*websocket.Conn]bool) 
// メッセージブロードキャストチャネル
var broadcast = make(chan Message)

// アップグレーダ
var upgrader = websocket.Upgrader{}

// メッセージ用構造体
type Message struct {
    Username string `json:"username"`
    Message  string `json:"message"`
}

func main() {
    // ファイルサーバー
    fs := http.FileServer(http.Dir("./public"))
    http.Handle("/", fs)

    // WebSocket
    http.HandleFunc("/ws", handleConnections)
    go handleMessages()

    err := http.ListenAndServe(":8080", nil)
    if err != nil {
        log.Fatal("ListenAndServe: ", err)
    }
}

func handleConnections(w http.ResponseWriter, r *http.Request) {
    // 送られてきたGETリクエストをWebSocketにアップグレード
    ws, err := upgrader.Upgrade(w, r, nil)
    if err != nil {
        log.Fatal(err)
    }
    defer ws.Close()

    // クライアントを登録
    clients[ws] = true

    for {
        var message Message
        // 新しいメッセージをJSONとして読み込み、Message構造体にマッピング
        err := ws.ReadJSON(&message)
        if err != nil {
            log.Printf("error: %v", err)
            delete(clients, ws)
            break
        }
        // 受け取ったメッセージをbroadcastチャネルに送る
        broadcast <- message
    }
}

func handleMessages() {
    for {
        // broadcastチャネルからメッセージを受け取る
        message := <-broadcast
        // 接続中の全クライアントにメッセージを送る
        for client := range clients {
            err := client.WriteJSON(message)
            if err != nil {
                log.Printf("error: %v", err)
                client.Close()
                delete(clients, client)
            }
        }
    }
}
