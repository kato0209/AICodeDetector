<?php
function dijkstraWithPriorityQueue($graph, $source) {
    $distance = [];
    $previous = [];
 <extra_id_0>  $queue = [];

    foreach ($graph as <extra_id_1> $value) <extra_id_2>       <extra_id_3> INF;
        $previous[$vertex] <extra_id_4>        <extra_id_5> INF;
    }

 <extra_id_6>  $distance[$source] = 0;
    $queue[$source] = 0;

    while (!empty($queue)) {
        asort($queue);
        $min = key($queue);
   <extra_id_7>    unset($queue[$min]);

        foreach ($graph[$min] as <extra_id_8> $cost) {
    