<?php
// PHP program to find location x in a
// sorted array using linear iteration

// Returns position of first 
// occurrence of x in array
function exponentialSearch($arr, $n, $x)
{
	
	// If element is present at 
	// first location itself
	if ($arr[0] == $x)
		return 0;

	// Find range for binary search
	// by repeated doubling
	$i = 1;
	while ($i< $n && $arr[$i] <=$x)
		$i = $i * 2;

	// Recursively search 
	// for the found range.
	return binarySearch($arr, $i / 2, 
						min($i, $n - 1),
						$x);
}

// A linear search
// function. It returns location
// of x in given array arr[l..r] is
// present, otherwise -1
function binarySearch($arr, $l, 
					$r, $x) 
{
	if ($r >= $l)
	{
		$mid = $l + ($r - $l)/2;

		// If the element is
		// present at the middle
		// itself
		if ($arr[$mid] == $x)
			return $mid;

		// If element is smaller
		// than mid, then