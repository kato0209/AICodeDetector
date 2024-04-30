package server

import (
	"encoding/xml"
	"io/ioutil"
	"net/smtp"
	"strings"
)

// ---------------------------------------
// SMTPサーバ情報取得
// ---------------------------------------
func SmtpServerConfig() (models.SmtpServerConfig, error) {

	var smtpServerInfo []byte
	var err error

	smtpServerInfo, err = ioutil.ReadFile("config/smtpserver.yaml")
	if err != nil {
		return models.SmtpServerConfig{}, err
	}

	var smtpConfig models.SmtpServerConfig
	err = yaml.Unmarshal([]byte(smtpServerInfo), &smtpConfig)
	if err != nil {
		return models.SmtpServerConfig{}, err
	}

	return smtpConfig, nil
}

// ---------------------------------------
// メール送信
// param1. 送信するメールアドレス  string
// param2. 送信するメールの件名   string
// param3. 送信するメールの本文   string
// return: error
// ---------------------------------------

func SmtpSendMail(mailAddress string, mailSubject string, mailBody string) error {

	var smtp models.SmtpServerConfig
	var smtpConn models.SmtpServerConfig

	smtpConn, err = SmtpServerConfig()
	if err != nil {
		return err
	}

	// メールの内容を定義
	toMailAddress := []string{mailAddress}

	// 本文を設定する
	var mailBody string

	mailMessage := []byte("To: " + mailAddress + "\r\n" +
		"Subject: " + mailSubject ) +
		"\r\n" +
		mailBody // SMTPサーバ接続
	var auth smtp.Auth
	auth = smtp.PlainAuth("", smtpConn.AuthAddress, smtpConn.AuthPassword, smtpConn.SmtpServer)

	// メール送信
	err = smtp.SendMail(smtpConn.SmtpServer+":"+smtpConn.SmtpPort, auth, smtpConn.AuthAddress, toMailAddress, mailMessage)
	if err != nil {
		return err
	}

	return nil
}

