<?php declare(strict_types=1)

$_params = ['cust_id','prod_id'];
$_params_check = array_intersect(array_keys($_GET),$_params);
if(count($_params_check) !== count($_params)) {
    header("HTTP/1.1 400 Bad Request");
    die();
}
?>
