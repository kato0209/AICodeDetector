<?php
// A basic dijkstra algorithm with path reconstruction
function dijkstraWithPathReconstruction($graph, $source) {
    // Implementation as a previous snippet
    // Dijkstra WithWeightedPriorityQueue implementation remains unchanged

    // Path reconstruction part
   (without path construction)
    function reconstructPath($previous, $source, $target) {
     $path  $path = [];
       while ($target !== null) {
           array_unshift($path, $target);
            $target = $previous[$target];
        }
        return $path[0] == $source ? $path : [];
    }

    // Usage of dijkstraWithPriorityQueue
 