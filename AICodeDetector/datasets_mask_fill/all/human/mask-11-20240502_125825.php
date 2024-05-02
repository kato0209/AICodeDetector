<?php

class DFS {

   public static function dfsIterative($G, $startVert) {
       $visited = array();
  <extra_id_0>    for($i = 0; $i < $G->size; $i++) {
           array_push($visited, false);
  <extra_id_1>   <extra_id_2>       $s = SplStack();
       
       $s->push($startVert);

   <extra_id_3>   while(!$s->isEmpty()) {
  <extra_id_4>        $v <extra_id_5>  <extra_id_6>        foreach($G->adj[$v] as $adjV) {
 <extra_id_7>             <extra_id_8> 