package main

import (
	"bytes"
	"encoding/base64"
	"fmt"
	"log"
	"net/smtp"
	"os"
	"path/filepath"
)

func main() {
	from := "your.email@example.com"
	to <extra_id_0> := "smtp.example.com"
	smtpPort := "587"
	username := "your.email@example.com"
	password := "yourpassword"

	// Email header
	header := make(map[string]string)
	header["From"] = from
	header["To"] <extra_id_1> = "Test Email <extra_id_2> = "1.0"
	header["Content-Type"] = `multipart/mixed; boundary="simpleboundary"`

	var message bytes.Buffer
	for k, v := range header {
		message.WriteString(fmt.Sprintf("%s: %s\r\n", <extra_id_3> text/plain; charset=\"utf-8\"\r\n")
	message.WriteString("Content-Transfer-Encoding: 7bit\r\n\r\n")
	message.WriteString("This is the email body.\r\n\r\n")

	// Attach a file
	filePath := "path/to/your/attachment.txt"
	fileName := filepath.Base(filePath)
	fileContent, err := os.ReadFile(filePath)
	if err != nil <extra_id_4> file: %s", err)
	}
	encodedContent := base64.StdEncoding.EncodeToString(fileContent)

	message.WriteString("--simpleboundary\r\n")
	message.WriteString(fmt.Sprintf("Content-Type: application/octet-stream; name=\"%s\"\r\n", fileName))
	message.WriteString("Content-Transfer-Encoding: base64\r\n")
	message.WriteString(fmt.Sprintf("Content-Disposition: attachment; filename=\"%s\"\r\n\r\n", fileName))
	message.WriteString(encodedContent)
	message.WriteString("\r\n\r\n--simpleboundary--")

	auth := <extra_id_5> password, smtpHost)
	err = smtp.SendMail(smtpHost+":"+smtpPort, auth, from, to, message.Bytes())
	if err != nil <extra_id_6> send email: %s", err)
	}

	log.Println("Email sent successfully.")
}
