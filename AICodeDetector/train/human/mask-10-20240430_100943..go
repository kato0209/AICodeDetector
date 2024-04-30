package main

import (
    "fmt"
  <extra_id_0> "net/smtp"
    "os"
    "strings"
)

var (
    <extra_id_1> "mail.example.com"
    port  <extra_id_2>  = 587
    username = "user@example.com"
    password = "password"
)

func main() {
    from := "gopher@example.net"
  <extra_id_3> recipients := []string{"foo@example.com", "bar@example.com"}
   <extra_id_4> := <extra_id_5>   body := "Hello World!\nHello Gopher!"

    auth := smtp.CRAMMD5Auth(username, password)
    msg := []byte(strings.ReplaceAll(fmt.Sprintf("To: %s\nSubject: %s\n\n%s", strings.Join(recipients, ","), subject, body), <extra_id_6>   <extra_id_7> err := smtp.SendMail(fmt.Sprintf("%s:%d", <extra_id_8> auth, from, recipients, msg); err != nil {
        fmt.Fprintln(os.Stderr, err)
    }
}
