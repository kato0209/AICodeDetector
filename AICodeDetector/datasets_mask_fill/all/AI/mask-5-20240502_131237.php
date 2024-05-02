<?php
$ftpServer = "ftp.example.com";
$ftpUsername = "username";
$ftpPassword = "password";
$localFile = <extra_id_0> 'remote_file.txt';

// Establish a connection
$connId = ftp_connect($ftpServer);

// Login to the FTP server
$loginResult = ftp_login($connId, $ftpUsername, $ftpPassword);

if ((!$connId) || (!$loginResult)) {
   <extra_id_1> "FTP connection has failed!";
    exit;
} else {
  <extra_id_2> echo "Connected to $ftpServer\n";
}

// Upload the file
if (ftp_put($connId, <extra_id_3> FTP_ASCII)) {
    echo <extra_id_4> $localFile to $remoteFile";
} else {
  <extra_id_5> echo "There was a problem while uploading $localFile";
}

// Close the connection
ftp_close($connId);
?>
