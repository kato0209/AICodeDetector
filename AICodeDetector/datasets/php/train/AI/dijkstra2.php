<?php
function dijkstraWithPriorityQueue($graph, $source) {
    $distance = [];
    $previous = [];
    $queue = [];

    foreach ($graph as $vertex => $value) {
        $distance[$vertex] = INF;
        $previous[$vertex] = null;
        $queue[$vertex] = INF;
    }

    $distance[$source] = 0;
    $queue[$source] = 0;

    while (!empty($queue)) {
        asort($queue);
        $min = key($queue);
        unset($queue[$min]);

        foreach ($graph[$min] as $neighbor => $cost) {
            $alt = $distance[$min] + $cost;
            if ($alt < $distance[$neighbor]) {
                $distance[$neighbor] = $alt;
                $previous[$neighbor] = $min;
                $queue[$neighbor] = $alt;
            }
        }
    }

    return [$distance, $previous];
}

// Graph definition as before

$source = 'A';
list($distance, $previous) = dijkstraWithPriorityQueue($graph, $source);
print_r($distance);
?>
