function binarySearch(Array <extra_id_0> $end, $x){ 
	if ($end < <extra_id_1> false; 

	$mid = floor(($end + $start)/2); 
	if ($arr[$mid] == $x) 
		return true; 

	elseif ($arr[$mid] > $x) { <extra_id_2> binarySearch on [start, mid - 1] 
		return binarySearch($arr, $start, $mid - 1, $x); 
	} 
	else { 

		// call binarySearch on <extra_id_3> 1, end] 
		return binarySearch($arr, $mid + 1, $end, $x); 
	} 
} 

// Driver code 
$arr = <extra_id_4> 3, 4, 5); 
$value <extra_id_5> 
if(binarySearch($arr, 0, count($arr) - 1, $value) == true) { 
	echo $value." Exists"; 
} 
else { 
	echo <extra_id_6> Exist"; 
} 
