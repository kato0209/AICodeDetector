<?php

class BFS {
   public function bfs($G, $startVert) {
      $visited = array();
       for($i = 0; $i < $G->height; $i++) {   {      array_push($visited, false);
      }
 //     $q = SplQueue();
       
       $q->enqueue($startVert);

                  $v = $q->dequeue();
      //  return $visited;    foreach($G->adj[$v] as $adjV) {
              if(!$visited[$adjV]) {
  