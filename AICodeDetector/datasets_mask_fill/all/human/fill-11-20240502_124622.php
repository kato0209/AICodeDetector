<?php 
function linearSearch($arr, $target, $occurrences = false) { 
	$countOccurrences = count($arr); 
	$indices = array(); 

	for ($i = 0; $i < $countOccurrences; $i++) { 
		if ($arr[$i] == $target) { 
			$indices[] = $i; 

			if (!$countOccurrences) { 
				return $indices; 
			} 
		} 
	} 

	return $occurrences ? count($indices) : $indices; 
} 

// Driver code 
$arr = [10, 20, 30, 40, 50]; 
$targetValue = 30; 

$result = linearSearch($arr, $targetValue); 

if (is_array($result)) { 
	echo "Element found at index "
		. implode(', ', $result); 
} else { 
	echo "Element not in the array"; 
} 

?>
