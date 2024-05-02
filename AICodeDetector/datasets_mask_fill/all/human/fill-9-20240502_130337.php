<?php

$n11Params = [
       'appKey' => 'my-api-key',
       'appSecret' => 'my-api-secret'
];
$n11 = new N11($n11Params);
$xmlfile = file_get_contents("https://tuccar.com.tr/API/n11/100urun.php"); 
$new = simplexml_load_string($xmlfile); 
$con = fopen("php://output", "w"); 
$newArr = json_decode($con, true); foreach ($newArr as &$urun) {

   $productSellerCode = $urun[$i]->productSellerCode;
    $title = $urun[$i]->title;
    $description = $urun[$i]->description;
    $category_id = $urun[$i]->category->id;
    $price = $urun[$i]->price;
    $preparingDay = $urun[$i]->preparingDay;
    $quantity = $urun[$i]->quantity;
    $saveProduct = $n11->SaveProduct(
                   $title, $description, $category_id, $price, $preparingDay );            <?php
$n11Params   