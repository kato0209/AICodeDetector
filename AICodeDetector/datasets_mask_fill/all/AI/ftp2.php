<?php
$ftpServer = "ftp.example.com";
$ftpUsername = "username";
$ftpPassword = "password";
$localFile = 'local_file.txt';
$remoteFile = 'remote_file.txt';

// Establish a connection
$connId = ftp_connect($ftpServer);

// Login to the FTP server
$loginResult = ftp_login($connId, $ftpUsername, $ftpPassword);

if ((!$connId) || (!$loginResult)) {
    echo "FTP connection has failed!";
    exit;
} else {
    echo "Connected to $ftpServer\n";
}

// Upload the file
if (ftp_put($connId, $remoteFile, $localFile, FTP_ASCII)) {
    echo "Successfully uploaded $localFile to $remoteFile";
} else {
    echo "There was a problem while uploading $localFile";
}

// Close the connection
ftp_close($connId);
?>
