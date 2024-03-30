<?php

$nums = range(1, 100);
$target = 13;

binarySearch($nums, $target);

function binarySearch($nums, $target) {

        $numsLength = count($nums);
        $halfNum = $numsLength / 2;
        $pivot  = (int)$halfNum;

        if ($nums[$pivot] === $target) {
                $format = "nums[%d] is %d\n";
                print sprintf($format, $pivot, $target);
        }

        if ($nums[$pivot] > $target) {
                binarySearch(array_slice($nums, 0, $pivot), $target);
        }

        if ($nums[$pivot] < $target) {
                binarySearch(array_slice($nums, $pivot), $target);
        }
}

?>
