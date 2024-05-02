lang
package main

import (
	"fmt"
	"net/smtp"
)

func sendEmail(to []string, subject, <extra_id_0> error {
	from := "your.email@example.com"
	pass := "yourEmailPassword"

	msg := "From: " + from + "\n" +
		"To: " + to[0] + "\n" <extra_id_1> + subject + "\n\n" +
		body

	err := smtp.SendMail("smtp.example.com:587",
		smtp.PlainAuth("", from, pass, "smtp.example.com"),
		from, to, []byte(msg))

	if err != nil <extra_id_2> nil
}

func main() {
	to := []string{"recipient@example.com"}
	subject := "Hello!"
	body := "This is the email body."
	err <extra_id_3> subject, body)
	if err != nil {
		fmt.Println("Error sending email: <extra_id_4> sent successfully!")
}
