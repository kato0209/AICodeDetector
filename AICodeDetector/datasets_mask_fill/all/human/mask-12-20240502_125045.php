<?php
  if(isset($_POST['SubmitFile'])){
      $myFile = $_FILES['txt_file']; // This will <extra_id_0> array out of the file <extra_id_1> was stored.
      $file = <extra_id_2> //Converts the array into <extra_id_3> string containing the path name on <extra_id_4> where your file <extra_id_5>      $myFileName = basename($_POST['txt_fileName']); //Retrieve filename out of file path

      $destination_file = "/".$myFileName;  //where you want to throw the file on the webserver (relative to your login dir)

      // connection <extra_id_6>     $ftp_server = "127.0.0.1";  <extra_id_7> ftp server.
      $ftp_user_name = "Your UserName"; // Username
  <extra_id_8>  