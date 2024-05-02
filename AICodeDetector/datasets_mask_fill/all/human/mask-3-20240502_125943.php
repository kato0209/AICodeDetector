<?php
    $encoding = "utf-8";

    // Preferences for Subject field
    <extra_id_0> array(
        "input-charset" => $encoding,
   <extra_id_1>    "output-charset" => $encoding,
   <extra_id_2>  <extra_id_3> "line-length" <extra_id_4>        "line-break-chars" => "\r\n"
    );

   <extra_id_5> Mail header
    $header = "Content-type: <extra_id_6> \r\n";
    $header .= "From: ".$from_name." <".$from_mail."> \r\n";
    $header .= "MIME-Version: 1.0 \r\n";
    <extra_id_7> "Content-Transfer-Encoding: 8bit \r\n";
    $header .= "Date: ".date("r (T)")." \r\n";
    $header .= iconv_mime_encode("Subject", $mail_subject, $subject_preferences);

   <extra_id_8> Send mail
