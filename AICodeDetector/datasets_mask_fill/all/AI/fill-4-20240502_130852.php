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

if (false == $connId || (!$loginResult)) {
    echo "FTP connection has failed!";
    exit;
} else {
    echo "Connected to $ftpServer\n";
}

// Try to download $remoteFile and save in $localFile
if (ftp_get($connId, $localFile, $remoteFile, FTP_ASCII)) {
    echo "Successfully downloaded file from $localFile";
} else {
    echo "There was a problem while downloading $remoteFile to $localFile!";
    exit;
}

// Close the FTP connection
ftp_close($connId);
?>
