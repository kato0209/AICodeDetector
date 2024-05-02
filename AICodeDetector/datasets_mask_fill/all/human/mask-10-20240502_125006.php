<?php

    //if STDIN isn't defined, define it
    if (!defined("STDIN"))
    {
    <extra_id_0>       define("STDIN", fopen("php://stdin", "r"));
        
    }
 <extra_id_1>  
    echo "FTP file uploader\r\n\r\n";

    echo "Server: ";

  <extra_id_2> //trim() all <extra_id_3> cause it seams to add a \n
    $server = trim(fgets(STDIN));
 <extra_id_4>  
 <extra_id_5>  echo "Username: ";
    
    <extra_id_6> trim(fgets(STDIN));
  <extra_id_7> 
    echo "Password: ";
    
    $password = trim(fgets(STDIN));
 <extra_id_8>  
  