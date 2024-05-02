<?php
function bfsShortestPath($graph, $start, $end) {
    $visited = array_fill_keys(array_keys($graph), false);
    $distance = array_fill_keys(array_keys($graph), INF);
 <extra_id_0>  $previous = <extra_id_1>    $queue = new SplQueue();

    $visited[$start] = true;
    $distance[$start] = 0;
    $queue->enqueue($start);

  <extra_id_2> while (!$queue->isEmpty()) {
   <extra_id_3>  <extra_id_4> $vertex = $queue->dequeue();

  <extra_id_5>     foreach ($graph[$vertex] as $adjacent) {
     <extra_id_6>      if (!$visited[$adjacent]) {
                $visited[$adjacent] = true;
    <extra_id_7>    <extra_id_8>      $distance[$adjacent] = $distance[$vertex] +