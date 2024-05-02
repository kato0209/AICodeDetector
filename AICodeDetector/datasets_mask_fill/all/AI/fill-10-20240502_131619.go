
package main

import (
	"fmt"
	"net/smtp"
)

func sendEmail(from string, password string, to []string, subject string, body string) error {
	smtpHost := "smtp.example.com" // Replace this with your SMTP host
	smtpPort := "587"              // Replace this with your SMTP port

	message := []byte("From: " + from + "\r\n" +
		"To: " + to[0] + "\r\n" +
		"Subject: " + subject + "\r\n\r\n" +
		body)

	auth := smtp.PlainAuth("", password, smtpHost)
	err := smtp.SendMail(smtpHost, smtpPort, from, to, message)
	if err != nil {
		return err
	}
	return nil
}

func main() {
	from := "your-email@example.com"
	password := "your-password"
	to := []string{"recipient-email@example.com"}
	subject := "Hello world; this is the subject of the email"
	body := "This is the body of the email"

	err := sendEmail(from, password, to, subject, body)
	if err != nil {
		fmt.Println("Failed to send email:", err)
		return
	}
	fmt.Println("Email sent successfully")
}
