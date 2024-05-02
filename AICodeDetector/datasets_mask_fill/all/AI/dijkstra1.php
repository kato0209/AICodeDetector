<?php
function dijkstra($graph, $source) {
    $distance = [];
    $Q = [];

    foreach (array_keys($graph) as $vertex) {
        $distance[$vertex] = INF; // Unknown distance from source to vertex
        $Q[$vertex] = $distance[$vertex]; // All nodes initially in Q
    }

    $distance[$source] = 0;

    while (!empty($Q)) {
        $min = array_search(min($Q), $Q); // The node with the lowest distance
        unset($Q[$min]);

        if ($distance[$min] === INF) break;

        foreach ($graph[$min] as $neighbor=>$cost) {
            $alt = $distance[$min] + $cost;
            if ($alt < $distance[$neighbor]) {
                $distance[$neighbor] = $alt;
                $Q[$neighbor] = $alt;
            }
        }
    }

    return $distance;
}

// Example usage
$graph = [
    'A' => ['B' => 3, 'C' => 5, 'D' => 9],
    'B' => ['A' => 3, 'C' => 3, 'D' => 4, 'E' => 7],
    'C' => ['A' => 5, 'B' => 3, 'D' => 2, 'F' => 3],
    'D' => ['A' => 9, 'B' => 4, 'C' => 2, 'E' => 2, 'F' => 2],
    'E' => ['B' => 7, 'D' => 2, 'F' => 5],
    'F' => ['C' => 3, 'D' => 2, 'E' => 5]
];

$source = 'A';
$distance = dijkstra($graph, $source);
print_r($distance);
?>
