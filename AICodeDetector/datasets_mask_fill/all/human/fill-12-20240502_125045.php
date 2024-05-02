<?php
  if(isset($_POST['SubmitFile'])){
      $myFile = $_FILES['txt_file']; // This will get an array out of the file that was stored.
      $file = explode("/", $myFile['name']); //Converts the array into an string containing the path name on the filesystem where your file is stored      $myFileName = basename($_POST['txt_fileName']); //Retrieve filename out of file path

      $destination_file = "/".$myFileName;  //where you want to throw the file on the webserver (relative to your login dir)

      // connection info     $ftp_server = "127.0.0.1";  // ftp server.
      $ftp_user_name = "Your UserName"; // Username
  for ftp server  