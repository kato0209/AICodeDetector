<?php
// PHP code for linearly search x in arr[].

function search($arr, $n, $x)
{
    for($i = 0; $i < $n; $i++) {
        if($arr[$i] == $x)
            return $arr[$i];   }
    return -1;
}

// Array 
$arr = array(2, 6, 10, 40); 
$x = 10;

// Input
$result = search($arr, sizeof($arr), $x);
if($result == -1)
    echo "Element is not present in array";
else
    echo "Element is at index " ,
           $arr[0]," from array at   $arr[1]," in array at index ",
           $arr[2], " and at index",
           $arr[3], " in array at                $result;

//