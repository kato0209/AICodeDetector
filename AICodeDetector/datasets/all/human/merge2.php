<?php
// Function to perform merge sort on an array
function merge_sort($my_array){
    // Base case: if the array has only one element, return it
    if(count($my_array) == 1 ) return $my_array;
    
    // Calculate the middle index of the array
    $mid = count($my_array) / 2;
    
    // Divide the array into two halves: left and right
    $left = array_slice($my_array, 0, $mid);
    $right = array_slice($my_array, $mid);
    
    // Recursively call merge_sort on each half
    $left = merge_sort($left);
    $right = merge_sort($right);
    
    // Merge the sorted halves
    return merge($left, $right);
}

// Function to merge two sorted arrays
function merge($left, $right){
    $res = array(); // Initialize an empty array to store the merged result
    
    // Compare elements from left and right arrays and merge them in sorted order
    while (count($left) > 0 && count($right) > 0){
        if($left[0] > $right[0]){
            $res[] = $right[0];
            $right = array_slice($right , 1);
        }else{
            $res[] = $left[0];
            $left = array_slice($left, 1);
        }
    }
    
    // If any elements are remaining in the left array, append them to the result
    while (count($left) > 0){
        $res[] = $left[0];
        $left = array_slice($left, 1);
    }
    
    // If any elements are remaining in the right array, append them to the result
    while (count($right) > 0){
        $res[] = $right[0];
        $right = array_slice($right, 1);
    }
    
    // Return the merged result
    return $res;
}

// Example usage:
$test_array = array(100, 54, 7, 2, 5, 4, 1); // Define an array
echo "Original Array : ";
echo implode(', ',$test_array ); // Print the original array
echo "\nSorted Array :"; 
echo implode(', ',merge_sort($test_array))."\n"; // Sort the array using merge sort and print the sorted array
?>
