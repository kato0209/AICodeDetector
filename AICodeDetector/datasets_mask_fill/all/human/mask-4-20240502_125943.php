function sendMail(
    string <extra_id_0>   string $mailMessage = MAIL_CONF["mailMessage"],
    string $subject    <extra_id_1> MAIL_CONF["subject"],
    string $toAddress   = MAIL_CONF["toAddress"],
    string $fromMail    = MAIL_CONF["fromMail"]
): bool {
    
 <extra_id_2>  $fileAttachment = trim($fileAttachment);
   <extra_id_3>           = $fromMail;
    $pathInfo     <extra_id_4> = pathinfo($fileAttachment);
    $attchmentName <extra_id_5> "attachment_".date("YmdHms").(
    (isset($pathInfo['extension']))? <extra_id_6> ""
    );
 <extra_id_7>  
    $attachment    = <extra_id_8>   $boundary      = "PHP-mixed-".md5(time());
  