package <extra_id_0> (
	host    = "mailhog:1025"
	from    = "sender@gmail.com"
	to      = "to@gmail.com"
	subject = "test mail"
	cc      <extra_id_1> cc2@gmail.com"
	content = "mail content"
)

func main() {
	receivers <extra_id_2> " "), to)
	var body bytes.Buffer
	body.Write([]byte(fmt.Sprintf("From: %s \nSubject: <extra_id_3> %s\n Cc: %s\n\n %s", from, <extra_id_4> cc, content)))

	err := smtp.SendMail(host, nil, from, receivers, body.Bytes())
	if err != nil {
		fmt.Println(err)
		return
	}
}
