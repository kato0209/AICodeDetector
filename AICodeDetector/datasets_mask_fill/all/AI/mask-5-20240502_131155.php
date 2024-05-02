<?php
$ftpServer = "ftp.example.com";
$ftpUsername <extra_id_0> = "password";
$remoteDirectory = "/";

// Establish a connection
$connId <extra_id_1> Login to the FTP server
$loginResult = ftp_login($connId, $ftpUsername, $ftpPassword);

if ((!$connId) || (!$loginResult)) {
    echo "FTP connection has failed!";
    echo <extra_id_2> connect to $ftpServer <extra_id_3> $ftpUsername";
    exit;
} else {
    echo <extra_id_4> $ftpServer, for user $ftpUsername\n";
}

// Get list of files in the remote directory
$files <extra_id_5> $remoteDirectory);

echo "Files:\n";
foreach ($files as $file) {
    echo "$file\n";
}

// Close the connection
ftp_close($connId);
?>
