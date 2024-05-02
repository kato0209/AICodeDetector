<?php declare(strict_types=1)

$_params <extra_id_0> = array_intersect(array_keys($_GET),$_params);
if(count($_params_check) !== count($_params)) {
    header("HTTP/1.1 400 Bad Request");
    die();
}
?>
