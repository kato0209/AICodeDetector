package chatserver

import (
    "bufio"
    "fmt"
    "net"
    "strings"
)

type Server struct {
    Port   int
    Clients map[*Client]bool
    Join   chan *Client
    Leave  chan *Client
    Msg    chan string
}

type Client struct {
    Socket net.Conn
    Msg    chan string
}

func NewServer(port int) *Server {
    return &Server{
        Port:   port,
        Clients: make(map[*Client]bool),
        Join:   make(chan *Client),
        Leave:  make(chan *Client),
        Msg:    make(chan string),
    }
}

func (s *Server) Start() {
    addr := fmt.Sprintf(":%d", s.Port)
    listener, err := net.Listen("tcp", addr)
    if err != nil {
        fmt.Println("Error starting server:", err)
        return
    }
    defer listener.Close()

    go s.handleMessages()

    for {
        conn, err := listener.Accept()
        if err != nil {
            fmt.Println("Error accepting connection:", err)
            continue
        }

        client := &Client{Socket: conn, Msg: make(chan string)}
        s.Join <- client

        go s.handleClient(client)
    }
}

func (s *Server) handleClient(client *Client) {
    defer client.Socket.Close()

    go func() {
        for msg := range client.Msg {
            client.Socket.Write([]byte(msg))
        }
    }()

    scanner := bufio.NewScanner(client.Socket)
    for scanner.Scan() {
        msg := scanner.Text()
        if strings.TrimSpace(msg) == "" {
            continue
        }
        s.Msg <- msg
    }

    s.Leave <- client
}

func (s *Server) handleMessages() {
    for {
        select {
        case client := <-s.Join:
            s.Clients[client] = true
            fmt.Println("New client joined")
        case client := <-s.Leave:
            if _, ok := s.Clients[client]; ok {
                delete(s.Clients, client)
                close(client.Msg)
                fmt.Println("Client left")
            }
        case msg := <-s.Msg:
            for client := range s.Clients {
                client.Msg <- msg
            }
        }
    }
}
