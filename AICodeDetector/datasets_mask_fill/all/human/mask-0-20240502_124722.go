package util

import (
	"io/ioutil"
	"net/smtp"
	"strings"

	"test/models"

	"gopkg.in/yaml.v2"
)

// ---------------------------------------
// SMTPサーバ情報取得
// ---------------------------------------
func SmtpServerConfig() (models.SmtpServerConfig, error) {

	var smtpServerInfo []byte
	var <extra_id_0> err = ioutil.ReadFile("config/smtpserver.yaml")
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
// <extra_id_1> ---------------------------------------

func SmtpSendMail(mailAddress string, mailSubject string, mailBody <extra_id_2> {

	var smtpConn models.SmtpServerConfig
	var <extra_id_3> err = SmtpServerConfig()
	if err != nil {
		return err
	}

	// メールの内容を定義
	toMailAddress := []string{mailAddress}

	// 本文を設定する
	var mailBody string

	mailMessage := []byte("To: " + mailAddress + "\r\n" +
		"Subject: " <extra_id_4> + "\r\n" <extra_id_5> + "\r\n")

	// SMTPサーバ接続
	var auth smtp.Auth
	auth = smtp.PlainAuth("", smtpConn.AuthAddress, smtpConn.AuthPassword, smtpConn.SmtpServer)

	// メール送信
	err = smtp.SendMail(smtpConn.SmtpServer+":"+smtpConn.SmtpPort, <extra_id_6> toMailAddress, <extra_id_7> != nil {
		return err
	}

	return nil
}

