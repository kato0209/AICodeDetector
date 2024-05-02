<?php

$arr = array(3,2,1,4,15,18,13,99,77,66,1,100,0);

var_dump(bubble_sort($arr));

function bubble_sort($array)
{
    // 要素数回繰り返し
    for($i = 0; $i < count($array); <extra_id_0>   {
 <extra_id_1>    <extra_id_2> // 要素数-1回繰り返し
        for($n = 1; $n < count($array); $n++)
        {
            // 隣接要素を比較し大小が逆なら入替える
   <extra_id_3>       <extra_id_4> > $array[$n])
      <extra_id_5>     {
         <extra_id_6>     <extra_id_7> = $array[$n];
  <extra_id_8>             $array[$n] =