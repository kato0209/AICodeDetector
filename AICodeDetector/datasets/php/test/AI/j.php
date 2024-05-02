<?php
// 配列
$array = array("apple" => "red", "banana" => "yellow");

// JSONにエンコード
$json = json_encode($array);
echo $json;

// JSONをデコード
$decoded = json_decode($json, true);
print_r($decoded);
?>
