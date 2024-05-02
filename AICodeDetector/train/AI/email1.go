package main

import (
	"fmt"
	"log"
	"net/smtp"
)

func main() {
	from := "your.email@example.com"
	to := []string{"recipient@example.com"}
	smtpHost := "smtp.example.com"
	smtpPort := "587"
	username := "your.email@example.com"
	password := "yourpassword"

	subject := "Simple Email Test"
	body := "Hello, this is a test email from Go!"

	message := fmt.Sprintf("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n%s", from, to[0], subject, body)

	auth := smtp.PlainAuth("", username, password, smtpHost)
	err := smtp.SendMail(smtpHost+":"+smtpPort, auth, from, to, []byte(message))
	if err != nil {
		log.Fatalf("Failed to send email: %s", err)
	}

	log.Println("Simple email sent successfully.")
}
