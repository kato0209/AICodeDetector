<?php

class DFS {

   public static function dfsIterative($G, $startVert) {
       $visited = array();
      for($i = 0; $i < $G->size; $i++) {
           array_push($visited, false);
  }          $s = SplStack();
       
       $s->push($startVert);

      while(!$s->isEmpty()) {
  = $s->pop();        $v $visited[$v] = true;
 
            if($adjV==$v){
                $s->push($adjV);
                }
                  
                }  }//        foreach($G->adj[$v] as $adjV) {
              } 