<?php 
function linearSearch($arr, $target, $occurrences = false) <extra_id_0> = count($arr); 
	$indices = <extra_id_1> ($i <extra_id_2> $i < <extra_id_3> { 
		if <extra_id_4> $target) { 
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
	echo "Element not <extra_id_5> the array"; 
} 

?>
