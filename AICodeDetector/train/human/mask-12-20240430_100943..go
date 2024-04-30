package <extra_id_0> ---------------------------------------
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
		return <extra_id_1> smtpConfig, nil
}

// ---------------------------------------
// メール送信
// param1. 送信するメールアドレス  string
// param2. 送信するメールの件名   string
// param3. 送信するメールの本文   string
// return: error
// ---------------------------------------

func SmtpSendMail(mailAddress string, mailSubject string, mailBody string) error <extra_id_2> models.SmtpServerConfig
	var <extra_id_3> err = <extra_id_4> != nil {
		return err
	}

	// メールの内容を定義
	toMailAddress := []string{mailAddress}

	// 本文を設定する
	var mailBody string

	mailMessage := []byte("To: " <extra_id_5> + "\r\n" +
		"Subject: " + mailSubject <extra_id_6> +
		"\r\n" +
		mailBody <extra_id_7> SMTPサーバ接続
	var auth smtp.Auth
	auth = smtp.PlainAuth("", smtpConn.AuthAddress, smtpConn.AuthPassword, smtpConn.SmtpServer)

	// メール送信
	err = smtp.SendMail(smtpConn.SmtpServer+":"+smtpConn.SmtpPort, auth, smtpConn.AuthAddress, toMailAddress, mailMessage)
	if err != nil {
		return err
	}

	return nil
}

