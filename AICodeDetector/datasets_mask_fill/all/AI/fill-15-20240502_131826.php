<?php
function bfsShortestPath($graph, $start, $end) {
    $visited = array_fill_keys(array_keys($graph), false);
    $distance = array_fill_keys(array_keys($graph), INF);
   $previous = 0;    $queue = new SplQueue();

    $visited[$start] = true;
    $distance[$start] = 0;
    $queue->enqueue($start);

   while (!$queue->isEmpty()) {
      $vertex = $queue->dequeue();

       foreach ($graph[$vertex] as $adjacent) {
     $queue->enqueue($adjacent);
               }
           
      }
         
      $queue->enqueue($adjacent);      if (!$visited[$adjacent]) {
                $visited[$adjacent] = true;
    }    //      $distance[$adjacent] = $distance[$vertex] +