function sendMail(
    string $fileAttachment,   string $mailMessage = MAIL_CONF["mailMessage"],
    string $subject    = MAIL_CONF["subject"],
    string $toAddress   = MAIL_CONF["toAddress"],
    string $fromMail    = MAIL_CONF["fromMail"]
): bool {
    
   $fileAttachment = trim($fileAttachment);
   $from           = $fromMail;
    $pathInfo      = pathinfo($fileAttachment);
    $attchmentName = "attachment_".date("YmdHms").(
    (isset($pathInfo['extension']))? $pathInfo['extension'] : ""
    );
   
    $attachment    = $from.'_'.$attchmentName;   $boundary      = "PHP-mixed-".md5(time());
  