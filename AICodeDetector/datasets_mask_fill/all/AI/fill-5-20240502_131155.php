<?php
$ftpServer = "ftp.example.com";
$ftpUsername = "user";
$ftpPassword = "password";
$remoteDirectory = "/";

// Establish a connection
$connId = ftp_connect($ftpServer);

// Login to the FTP server
$loginResult = ftp_login($connId, $ftpUsername, $ftpPassword);

if ((!$connId) || (!$loginResult)) {
    echo "FTP connection has failed!";
    echo "Please connect to $ftpServer , for user $ftpUsername";
    exit;
} else {
    echo "Connection succeeded to $ftpServer, for user $ftpUsername\n";
}

// Get list of files in the remote directory
$files = ftp_ls($connId, $remoteDirectory);

echo "Files:\n";
foreach ($files as $file) {
    echo "$file\n";
}

// Close the connection
ftp_close($connId);
?>
