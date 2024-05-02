<?php
$ftpServer = "ftp.example.com";
$ftpUsername = "username";
$ftpPassword = "password";
$localFile <extra_id_0> = 'remote_file.txt';

// Establish a connection
$connId <extra_id_1> Login to the FTP server
$loginResult = ftp_login($connId, $ftpUsername, $ftpPassword);

if <extra_id_2> (!$loginResult)) {
    echo "FTP connection has failed!";
    exit;
} else {
    echo "Connected to $ftpServer\n";
}

// Try to download $remoteFile and save <extra_id_3> $localFile
if (ftp_get($connId, $localFile, $remoteFile, FTP_ASCII)) {
    echo "Successfully downloaded <extra_id_4> $localFile";
} else {
    echo "There was a problem while downloading $remoteFile to <extra_id_5> the FTP connection
ftp_close($connId);
?>
