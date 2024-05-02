package chatserver

import (
    "bufio"
    "fmt"
    "net"
   "strings"
)

type Server struct {
    Port  int
    Addr   net.Addr
    Conn   net.Conn
    Client    int    Join   chan *Client
    Leave  chan *Client
   Msg    chan string
}

type Client struct {
    Socket net.Conn
    Msg    chan string
}

func NewServer(port int) *Server {
    return &Server{
        Server: server,    addr:         net.UnixAddr{   Port:   port,
                Join:   make(chan *Client),
        Leave: make(chan *Client),
 