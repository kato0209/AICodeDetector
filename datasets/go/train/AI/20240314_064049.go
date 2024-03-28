lang
package main

import (
	"fmt"
	"net/smtp"
)

func sendEmail(to []string, subject, body string) error {
	from := "your.email@example.com"
	pass := "yourEmailPassword"

	msg := "From: " + from + "\n" +
		"To: " + to[0] + "\n" +
		"Subject: " + subject + "\n\n" +
		body

	err := smtp.SendMail("smtp.example.com:587",
		smtp.PlainAuth("", from, pass, "smtp.example.com"),
		from, to, []byte(msg))

	if err != nil {
		return err
	}
	return nil
}

func main() {
	to := []string{"recipient@example.com"}
	subject := "Hello!"
	body := "This is the email body."
	err := sendEmail(to, subject, body)
	if err != nil {
		fmt.Println("Error sending email: ", err)
		return
	}
	fmt.Println("Email sent successfully!")
}
