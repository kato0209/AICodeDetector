
package main

import (
	"fmt"
	"net/smtp"
)

func sendEmail(to []string, subject, body string) error {
	from := "your-email@gmail.com"
	password := "your-email-password"

	// SMTP server configuration.
	smtpHost := "smtp.gmail.com"
	smtpPort := "587"

	// Message.
	message := []byte("To: " + to[0] + "\r\n" +
		"Subject: " + subject + "\r\n" +
		"\r\n" +
		body + "\r\n")

	// Authentication.
	auth := smtp.PlainAuth("", from, password, smtpHost)

	// Sending email.
	err := smtp.SendMail(smtpHost+":"+smtpPort, auth, from, to, message)
	if err != nil {
		return err
	}
	return nil
}

func main() {
	to := []string{"recipient-email@example.com"}
	subject := "Hello!"
	body := "This is a test email body."
	err := sendEmail(to, subject, body)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println("Email sent successfully!")
}
