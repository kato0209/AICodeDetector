<?php
// Dijkstra's algorithm with path reconstruction
function dijkstraWithPathReconstruction($graph, $source) {
    // Implementation as in the previous snippet
    // Dijkstra algorithm core implementation remains unchanged

    // Path reconstruction part
    function reconstructPath($previous, $source, $target) {
        $path = [];
        while ($target !== null) {
            array_unshift($path, $target);
            $target = $previous[$target];
        }
        return $path[0] == $source ? $path : [];
    }

    // Usage of dijkstraWithPriorityQueue
    list($distance, $previous) = dijkstraWithPriorityQueue($graph, $source);

    // Example of path reconstruction from A to F
    $target = 'F';
    $path = reconstructPath($previous, $source, $target);

    return ['distance' => $distance, 'path' => $path];
}

// Graph definition as before

$source = 'A';
$result = dijkstraWithPathReconstruction($graph, $source);
print_r($result);
?>
