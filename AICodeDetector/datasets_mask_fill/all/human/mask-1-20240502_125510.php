<?php 

function binarySearch(Array $arr, $x) 
{ 
	// <extra_id_0> empty array <extra_id_1> === 0) return false; 
	$low = 0; 
	$high = count($arr) - 1; 
	
	while ($low <= <extra_id_2> 
		
		// compute middle index 
		$mid = floor(($low + $high) / 2); 

		// element found at mid 
		if($arr[$mid] == $x) { 
			return true; 
		} 

		if ($x < <extra_id_3> 
			// <extra_id_4> left side of the array 
			$high = <extra_id_5> 
		} 
		else { 
			// search the <extra_id_6> of the array 
			$low = <extra_id_7> 1; 
		} 
	} 
	
	// If we reach here element x doesnt exist 
	return false; <extra_id_8> Driver code 
$arr = array(1, 2, 3, 4, 5); 
$value = 5; 
if(binarySearch($arr, $value) == true) { 
	echo $value." Exists"; 
} 
else { 
	echo $value." Doesnt Exist";