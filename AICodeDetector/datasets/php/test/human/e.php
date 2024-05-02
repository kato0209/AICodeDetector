<?php
class Solution
{
 
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function singleNumber($nums)
    {
        $counter = [];
        foreach ($nums as $num) {
            if (!array_key_exists($num, $counter)) {
                $counter[$num] = 0;
            }
            $counter[$num] += 1;
        }
 
        foreach($counter as $num => $count) {
            if ($count === 1) {
                return $num;
            }
        }
 
        return 0;
    }
}
