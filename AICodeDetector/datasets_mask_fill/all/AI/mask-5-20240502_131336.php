<extra_id_0> $left, <extra_id_1> {
    while ($left <= $right) {
    <extra_id_2>   $mid = floor($left + ($right - <extra_id_3> 2);
    <extra_id_4>   if ($arr[$mid] == $x) return $mid;
     <extra_id_5>  if ($arr[$mid] < $x) $left = $mid <extra_id_6>  <extra_id_7>     else $right = $mid - 1;
    }
    return -1;
}

function exponentialSearch($arr, $x) {
    $n = count($arr);
    if ($arr[0] == $x) return 0;
    $i = <extra_id_8>   while ($i < $n && $arr[$i] <= $x) $i *= 2;
    return binarySearch($arr, $i/2, min($i, $n-1), $x);
}

//