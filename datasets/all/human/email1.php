function sendMail(
    string $fileAttachment,
    string $mailMessage = MAIL_CONF["mailMessage"],
    string $subject     = MAIL_CONF["subject"],
    string $toAddress   = MAIL_CONF["toAddress"],
    string $fromMail    = MAIL_CONF["fromMail"]
): bool {
    
    $fileAttachment = trim($fileAttachment);
    $from           = $fromMail;
    $pathInfo       = pathinfo($fileAttachment);
    $attchmentName  = "attachment_".date("YmdHms").(
    (isset($pathInfo['extension']))? ".".$pathInfo['extension'] : ""
    );
    
    $attachment    = chunk_split(base64_encode(file_get_contents($fileAttachment)));
    $boundary      = "PHP-mixed-".md5(time());
    $boundWithPre  = "\n--".$boundary;
    
    $headers   = "From: $from";
    $headers  .= "\nReply-To: $from";
    $headers  .= "\nContent-Type: multipart/mixed; boundary=\"".$boundary."\"";
    
    $message   = $boundWithPre;
    $message  .= "\n Content-Type: text/plain; charset=UTF-8\n";
    $message  .= "\n $mailMessage";
    
    $message .= $boundWithPre;
    $message .= "\nContent-Type: application/octet-stream; name=\"".$attchmentName."\"";
    $message .= "\nContent-Transfer-Encoding: base64\n";
    $message .= "\nContent-Disposition: attachment\n";
    $message .= $attachment;
    $message .= $boundWithPre."--";
    
    return mail($toAddress, $subject, $message, $headers);
}

* Sending email in html

function sendHtmlMail(
    string $mailMessage = MAIL_CONF["mailMessage"],
    string $subject     = MAIL_CONF["subject"],
    array $toAddress    = MAIL_CONF["toAddress"],
    string $fromMail    = MAIL_CONF["fromMail"]
): bool {
    
    $to        = implode(",", $toAddress);
    $headers[] = 'MIME-Version: 1.0';
    $headers[] = 'Content-type: text/html; charset=iso-8859-1';    
    $headers[] = 'To: '.$to;
    $headers[] = 'From: '.$fromMail;    

    return mail($to, $subject, $mailMessage, implode("\r\n", $headers));
}
