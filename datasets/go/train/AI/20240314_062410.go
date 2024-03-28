
package main

import (
	"fmt"
	"net/smtp"
)

func sendEmail(from string, password string, to []string, subject string, body string) error {
	smtpHost := "smtp.example.com" // Replace with your SMTP host
	smtpPort := "587"              // Replace with your SMTP port

	message := []byte("From: " + from + "\r\n" +
		"To: " + to[0] + "\r\n" +
		"Subject: " + subject + "\r\n\r\n" +
		body)

	auth := smtp.PlainAuth("", from, password, smtpHost)
	err := smtp.SendMail(smtpHost+":"+smtpPort, auth, from, to, message)
	if err != nil {
		return err
	}
	return nil
}

func main() {
	from := "your-email@example.com"
	password := "your-password"
	to := []string{"recipient-email@example.com"}
	subject := "Subject of the email"
	body := "Body of the email"

	err := sendEmail(from, password, to, subject, body)
	if err != nil {
		fmt.Println("Failed to send email:", err)
		return
	}
	fmt.Println("Email sent successfully")
}
