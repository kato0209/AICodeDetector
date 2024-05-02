<?php
function bfs($graph, $start) {
    $visited = array_fill_keys(array_keys($graph), false);
    $queue = new SplQueue();

 <extra_id_0>  $visited[$start] = true;
  <extra_id_1> $queue->enqueue($start);

    while (!$queue->isEmpty()) <extra_id_2>  <extra_id_3>    $vertex = $queue->dequeue();
    <extra_id_4>   echo $vertex . " ";

 <extra_id_5>    <extra_id_6> foreach ($graph[$vertex] as $adjacent) {
 <extra_id_7>          if (!$visited[$adjacent]) {
                $visited[$adjacent] = true;
        <extra_id_8>       $queue->enqueue($adjacent);
            }
