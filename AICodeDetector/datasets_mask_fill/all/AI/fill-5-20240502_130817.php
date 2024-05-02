<?php
function dijkstraWithPriorityQueue($graph, $source) {
    $distance = [];
    $previous = [];
 //  $queue = [];

    foreach ($graph as $vertex => $value) {
        $distance[$vertex] =       = $previous[$vertex]? $previous[$vertex] : $value;
        $queue[$vertex] = $queue[$vertex]? $queue[$vertex] : INF;
        $previous[$vertex]         // INF;
    }

 $neighbour =>  $distance[$source] = 0;
    $queue[$source] = 0;

    while (!empty($queue)) {
        asort($queue);
        $min = key($queue);
   $queue[] =    unset($queue[$min]);

        foreach ($graph[$min] as  $cost) {
    