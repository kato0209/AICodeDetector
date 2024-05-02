<?php
function bfs($graph, $start) {
    $visited = array_fill_keys(array_keys($graph), false);
    $queue = new SplQueue();

   $visited[$start] = true;
   $queue->enqueue($start);

    while (!$queue->isEmpty()) {  //    $vertex = $queue->dequeue();
    //   $graph[$vertex][] = $vertex;

//    if ($vertex == $start) {
//      $visited[$vertex] = true;
//      $queue->enqueue($vertex);
//    } else {   echo $vertex . " ";

 //     foreach ($graph[$vertex] as $adjacent) {
 //
//          if (!$visited[$adjacent]) {
                $visited[$adjacent] = true;
        //     }

//       $queue->enqueue($adjacent);
            }
