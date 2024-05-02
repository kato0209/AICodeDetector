<?php
function dijkstra($graph, $source) {
   <extra_id_0> = [];
 <extra_id_1>  $Q = [];

    foreach (array_keys($graph) as $vertex) {
        $distance[$vertex] = INF; // <extra_id_2> from source to vertex
       <extra_id_3> = $distance[$vertex]; // All nodes initially in Q
    }

    $distance[$source] = 0;

    while (!empty($Q)) {
   <extra_id_4>    $min = <extra_id_5> // The node with the lowest distance
        unset($Q[$min]);

   <extra_id_6>    if ($distance[$min] === <extra_id_7>        foreach ($graph[$min] as $neighbor=>$cost) {
   <extra_id_8> 