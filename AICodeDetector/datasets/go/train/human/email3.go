package main

import (
	"bytes"
	"fmt"
	"net/smtp"
	"strings"
)

const (
	host    = "mailhog:1025"
	from    = "sender@gmail.com"
	to      = "to@gmail.com"
	subject = "test mail"
	cc      = "cc1@gmail.com cc2@gmail.com"
	content = "mail content"
)

func main() {
	receivers := append(strings.Split(cc, " "), to)
	var body bytes.Buffer
	body.Write([]byte(fmt.Sprintf("From: %s \nSubject: %s \nTo: %s\n Cc: %s\n\n %s", from, subject, to, cc, content)))

	err := smtp.SendMail(host, nil, from, receivers, body.Bytes())
	if err != nil {
		fmt.Println(err)
		return
	}
}
