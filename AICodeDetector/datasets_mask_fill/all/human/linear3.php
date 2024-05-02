<?php 

function linearSearch($arr, $target) { 
	$length = count($arr); 

	for ($i = 0; $i < $length; $i++) { 
		if ($arr[$i] == $target) { 
			
			// Return index of target element 
			return $i; 
		} 
	} 

	// Return -1 if target element 
	// is not found 
	return -1; 
} 

// Driver code 
$arr = [10, 20, 30, 40, 50]; 
$targetValue = 30; 

$result = linearSearch($arr, $targetValue); 

if ($result != -1) { 
	echo "Element found at index $result"; 
} else { 
	echo "Element not found in the array"; 
} 

?>
