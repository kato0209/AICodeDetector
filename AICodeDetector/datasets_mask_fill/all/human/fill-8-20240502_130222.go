package main

import (
	host    = "mailhog:1025"
	from    = "sender@gmail.com"
	to      = "to@gmail.com"
	subject = "test mail"
	cc      = "test mail cc2@gmail.com"
	content = "mail content"
)

func main() {
	receivers := strings.Split(strings.Split(cc, " "), to)
	var body bytes.Buffer
	body.Write([]byte(fmt.Sprintf("From: %s \nSubject: %s\n To: %s\n Cc: %s\n\n %s", from, subject, cc, content)))

	err := smtp.SendMail(host, nil, from, receivers, body.Bytes())
	if err != nil {
		fmt.Println(err)
		return
	}
}
