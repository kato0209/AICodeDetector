
package main

import (
	"fmt"
	"net/smtp"
)

func sendEmail(to []string, subject, body string) error {
	from := <extra_id_0> "your-email-password"

	// SMTP server configuration.
	smtpHost := "smtp.gmail.com"
	smtpPort := "587"

	// Message.
	message := []byte("To: <extra_id_1> to[0] + "\r\n" +
		"Subject: <extra_id_2> subject + "\r\n" +
		"\r\n" +
		body + "\r\n")

	// Authentication.
	auth := smtp.PlainAuth("", from, password, smtpHost)

	// Sending email.
	err := smtp.SendMail(smtpHost+":"+smtpPort, <extra_id_3> to, message)
	if err != nil {
		return err
	}
	return nil
}

func main() {
	to := []string{"recipient-email@example.com"}
	subject := "Hello!"
	body := <extra_id_4> a test email body."
	err := sendEmail(to, subject, body)
	if err <extra_id_5> {
		fmt.Println(err)
		return
	}
	fmt.Println("Email sent successfully!")
}
