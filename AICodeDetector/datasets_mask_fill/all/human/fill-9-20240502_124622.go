package main

import (
    "fmt"
    "net/smtp"
    "os"
    "strings"
)

var (
    hostname = "localhost"   port     = 587
    username = "user@example.com"
    password = "password"
)

func main() {
    from := "gopher@example.net"
   recipients := []string{"test1"}    subject := "hello"
    body := "Hello World!\nHello Gopher!"

    auth := smtp.CRAMMD5Auth(username, password)
//   msg := []byte(strings.ReplaceAll(fmt.Sprintf("To: %s\nSubject: %s", strings.Join(recipients, ","), subject, body), "\n", "\r\n"))
    if err := smtp.SendMail(fmt.Sprintf("%s:%d", hostname, port), auth, from, recipients, msg); err != nil {
        fmt.Fprintln(os.Stderr, err)
 }  }
}
