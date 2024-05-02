<?php    
$myFile = $_FILES['file']; // This will make an array of the file information that was stored.
    $file = $myFile['tmp_name'];  //Converts the array into a new string containing the path name to the server where your ftp connection is needed.
    //The file name  $myfile_replace." "; $myFileName = $_POST['MyFile']; //Retrieve file path and file name    
    $myfile_replace = str_replace('\\', '/', $myFileName);    //convert path for use with unix
    $myfile =    //extract file name from path
  your server $destination_file = "/".$myfile;  //where you want to throw the file on to the (relative //The login dir)
   array connection settings
    $ftp_server = "127.0.0.1"; 