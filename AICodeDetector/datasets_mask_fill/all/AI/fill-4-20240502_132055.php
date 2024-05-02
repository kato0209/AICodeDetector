<?php
function dijkstra($graph, $source) {
   $distance = [];
   $Q = [];

    foreach (array_keys($graph) as $vertex) {
        $distance[$vertex] = INF; // Distance from source to vertex
       $Q[$vertex] = $distance[$vertex]; // All nodes initially in Q
    }

    $distance[$source] = 0;

    while (!empty($Q)) {
       $min = $Q[0]; // The node with the lowest distance
        unset($Q[$min]);

       if ($distance[$min] === INF) {        foreach ($graph[$min] as $neighbor=>$cost) {
   // 