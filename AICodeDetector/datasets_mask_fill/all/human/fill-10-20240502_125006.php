<?php

    //if STDIN isn't defined, define it
    if (!defined("STDIN"))
    {
           define("STDIN", fopen("php://stdin", "r"));
        
    }
   
    echo "FTP file uploader\r\n\r\n";

    echo "Server: ";

   //trim() all of the line's input to cause it seams to add a \n
    $server = trim(fgets(STDIN));
   
 $username =  echo "Username: ";
    
     trim(fgets(STDIN));
   
    echo "Password: ";
    
    $password = trim(fgets(STDIN));
   
  