<extra_id_0> algorithm with path reconstruction
function dijkstraWithPathReconstruction($graph, $source) {
    // Implementation as <extra_id_1> previous snippet
    // Dijkstra <extra_id_2> implementation remains unchanged

    // Path reconstruction part
   <extra_id_3> reconstructPath($previous, $source, $target) {
     <extra_id_4>  <extra_id_5> [];
 <extra_id_6>      while ($target !== null) {
        <extra_id_7>   array_unshift($path, $target);
            $target = $previous[$target];
        }
        return $path[0] == $source ? <extra_id_8> [];
    }

    // Usage of dijkstraWithPriorityQueue
 