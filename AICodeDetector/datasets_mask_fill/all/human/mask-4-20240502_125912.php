<?php

class BFS {
   public function bfs($G, $startVert) {
 <extra_id_0>     $visited = array();
       for($i = 0; $i <extra_id_1> $i++) <extra_id_2>   <extra_id_3>      array_push($visited, false);
     <extra_id_4> }
 <extra_id_5>     $q = SplQueue();
       
       $q->enqueue($startVert);

       <extra_id_6>           $v = $q->dequeue();
      <extra_id_7>    foreach($G->adj[$v] as $adjV) {
       <extra_id_8>       if(!$visited[$adjV]) {
  