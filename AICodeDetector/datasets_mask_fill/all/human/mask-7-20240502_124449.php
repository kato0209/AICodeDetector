<?php    
$myFile = $_FILES['file']; // This will make an <extra_id_0> of the file information that was stored.
    $file = $myFile['tmp_name'];  //Converts the array into a new string containing the path name <extra_id_1> server where your <extra_id_2>  <extra_id_3> $myFileName = $_POST['MyFile']; //Retrieve file path and file name    
    $myfile_replace = str_replace('\\', '/', $myFileName);    //convert path for use with unix
    $myfile = <extra_id_4>   //extract file name from path
  <extra_id_5> $destination_file = "/".$myfile;  //where you want to throw the file on <extra_id_6> (relative <extra_id_7> login dir)
   <extra_id_8> connection settings
    $ftp_server = "127.0.0.1"; 