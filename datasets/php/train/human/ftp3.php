<?php

    //if STDIN isn't defined, define it
    if (!defined("STDIN"))
    {
    
        define("STDIN", fopen("php://stdin", "r"));
        
    }
    
    echo "FTP file uploader\r\n\r\n";

    echo "Server: ";

    //trim() all the fgets cause it seams to add a \n
    $server = trim(fgets(STDIN));
    
    echo "Username: ";
    
    $username = trim(fgets(STDIN));
    
    echo "Password: ";
    
    $password = trim(fgets(STDIN));
    
    $connect = ftp_connect($server);
    $login = ftp_login($connect, $username, $password);
    
    if ((!$connect) || (!$login))
    {
    
        exit("Login failed.\r\n");
        
    }
    
    echo "Connected\r\n";

    echo "PASV (Y/Any key = Off): ";
    
    if(trim(fgets(STDIN)) == "Y")
    {

        //enable passive mode
        ftp_pasv($connect, true);
    
            echo "PASV: On\r\n";
        
    }
    else
    {
    
        echo "PASV: Off\r\n";

    }

    $showContent = ftp_nlist($connect, "");
    
    echo "Listing Contents:\r\n";
        
        var_dump($showContent);

    echo "File to upload: ";
    
    $file = trim(fgets(STDIN));
    
    //escape the uploading process by typing "exit;"
    if ($file == "exit;")
    {
    
        exit;
    
    }
    
    //use "$file, $file" since the file shouldn't be renamed, also if its a binary file change the last argument to FTP_BINARY
    $upload = ftp_put($connect, $file, $file, FTP_ASCII);
    
    if (!$upload)
    {
    
        exit("Upload failed.\r\n");
        
    }
    else
    {
    
        echo "The file \"" . $file . "\" was successfully uploaded. :)\r\nSize of \"" . $file . "\": " . filesize($file) / 1024 ."kb.\r\n";
        echo "My work is done, bye.\r\n";
        
    }
    
    ftp_close($connect);

?>
