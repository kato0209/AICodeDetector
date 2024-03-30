<?php
$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "myDB";

// MySQLへ接続する
$conn = new mysqli($servername, $username, $password, $dbname);

// 接続チェック
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
echo "Connected successfully";
$conn->close();
?>
