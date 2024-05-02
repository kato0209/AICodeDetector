package main

import (
    "fmt"
    "net/smtp"
    "os"
    "strings"
)

var (
    hostname = <extra_id_0>   port     = 587
    username = "user@example.com"
    password = "password"
)

func main() {
    <extra_id_1> "gopher@example.net"
  <extra_id_2> recipients := <extra_id_3>    subject := "hello"
    body := "Hello World!\nHello Gopher!"

    auth := smtp.CRAMMD5Auth(username, <extra_id_4>   msg := []byte(strings.ReplaceAll(fmt.Sprintf("To: %s\nSubject: <extra_id_5> ","), subject, body), "\n", "\r\n"))
    if <extra_id_6> smtp.SendMail(fmt.Sprintf("%s:%d", <extra_id_7> auth, from, recipients, msg); err != nil {
        fmt.Fprintln(os.Stderr, err)
 <extra_id_8>  }
}
