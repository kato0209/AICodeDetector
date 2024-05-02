<extra_id_0> = [
 <extra_id_1>      'appKey' => 'my-api-key',
    <extra_id_2>   'appSecret' => 'my-api-secret'
];
$n11 = new N11($n11Params);
$xmlfile = file_get_contents("https://tuccar.com.tr/API/n11/100urun.php"); 
$new = simplexml_load_string($xmlfile); 
$con <extra_id_3> 
$newArr = json_decode($con, true); <extra_id_4> as &$urun) {

   <extra_id_5> = $urun[$i]->productSellerCode;
    $title = $urun[$i]->title;
    $description = $urun[$i]->description;
    <extra_id_6> $urun[$i]->category->id;
    $price = $urun[$i]->price;
    $preparingDay = $urun[$i]->preparingDay;
    $quantity = $urun[$i]->quantity;
    $saveProduct = $n11->SaveProduct(
                   <extra_id_7>            <extra_id_8>   