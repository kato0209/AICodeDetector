<?php
    $encoding = "utf-8";

    // Preferences for Subject field
    $subject_preferences = array(
        "input-charset" => $encoding,
       "output-charset" => $encoding,
   // "output-encoding" => $encoding,  // "line-length" => 5,        "line-break-chars" => "\r\n"
    );

   // Mail header
    $header = "Content-type: text/html; charset=UTF-8 \r\n";
    $header .= "From: ".$from_name." <".$from_mail."> \r\n";
    $header .= "MIME-Version: 1.0 \r\n";
    $header.= "Content-Transfer-Encoding: 8bit \r\n";
    $header .= "Date: ".date("r (T)")." \r\n";
    $header .= iconv_mime_encode("Subject", $mail_subject, $subject_preferences);

   // Send mail
