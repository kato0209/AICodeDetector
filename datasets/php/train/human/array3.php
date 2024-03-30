<?php
include "class.n11.php";
$n11Params = [
        'appKey' => 'my-api-key',
        'appSecret' => 'my-api-secret'
];
$n11 = new N11($n11Params);
$xmlfile = file_get_contents("https://tuccar.com.tr/API/n11/100urun.php"); 
$new = simplexml_load_string($xmlfile); 
$con = json_encode($new,JSON_UNESCAPED_UNICODE); 
$newArr = json_decode($con, true); 

foreach ($newArr as &$urun) {

    $productSellerCode = $urun[$i]->productSellerCode;
    $title = $urun[$i]->title;
    $description = $urun[$i]->description;
    $categoryid = $urun[$i]->category->id;
    $price = $urun[$i]->price;
    $preparingDay = $urun[$i]->preparingDay;
    $quantity = $urun[$i]->quantity;
    $saveProduct = $n11->SaveProduct(
                    [
                    'productSellerCode' => $productSellerCode,
                    'title' => $title,
                    'subtitle' => 'Stoktan hızlı kargo',
                    'description' => $description,
                    'category' =>
                    [
                        'id' => $categoryid
                    ],
                    'attributes' =>
                    [
                        'attribute' =>

                            foreach($urun->attributes as $attribute){
                                    'name' => $attribute['name'],
                                    'value' => $attribute['value']
                                    }
                    ],
                    'price' => $price,
                    'domestic' => false,
                    'currencyType' => 'TL',
                    'images' =>
                    [
                        'image' =>

                            foreach($urun->images as $image){
                                    'url' => $image['url'],
                                    'order' => $image['order']
                                    }
                    ],
                    'saleStartDate' => '',
                    'saleEndDate' => '',
                    'productionDate' => '',
                    'expirationDate' => '',
                    'productCondition' => '1',
                    'preparingDay' => $preparingDay,
                    'discount' => '',
                    'shipmentTemplate' => 'kargo-bizden',
                    'stockItems' =>
                    [
                        'stockItem' =>
                        [
                            'quantity' => $quantity,
                            'sellerStockCode' => '',
                            'attributes' =>
                            [
                                'attribute' => []
                            ],
                            'optionPrice' => ''
                        ]
                    ]
                ]
    );

} var_dump($saveProduct);
