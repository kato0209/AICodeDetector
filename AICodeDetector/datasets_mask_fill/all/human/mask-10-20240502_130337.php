<?php
// PHP program to find <extra_id_0> x in a
// sorted array using <extra_id_1> Returns <extra_id_2> first 
// occurrence of x in array
function exponentialSearch($arr, $n, $x)
{
	
	// <extra_id_3> is present at 
	// first location itself
	if ($arr[0] == $x)
		return 0;

	// Find range for binary search
	// by repeated doubling
	$i = 1;
	while ($i< $n <extra_id_4> <=$x)
		$i = $i * 2;

	// <extra_id_5> search 
	// for the found range.
	return binarySearch($arr, $i / 2, 
						min($i, $n - <extra_id_6> A <extra_id_7> search
// function. It returns location
// of x in given array arr[l..r] is
// present, otherwise -1
function binarySearch($arr, $l, 
					$r, <extra_id_8> >= $l)
	{
		$mid = $l + ($r - $l)/2;

		// If the element is
		// present at the middle
		// itself
		if ($arr[$mid] == $x)
			return $mid;

		// If element is smaller
		// than mid, then