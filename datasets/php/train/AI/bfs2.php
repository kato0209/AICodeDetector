<?php
function bfsShortestPath($graph, $start, $end) {
    $visited = array_fill_keys(array_keys($graph), false);
    $distance = array_fill_keys(array_keys($graph), INF);
    $previous = array_fill_keys(array_keys($graph), null);
    $queue = new SplQueue();

    $visited[$start] = true;
    $distance[$start] = 0;
    $queue->enqueue($start);

    while (!$queue->isEmpty()) {
        $vertex = $queue->dequeue();

        foreach ($graph[$vertex] as $adjacent) {
            if (!$visited[$adjacent]) {
                $visited[$adjacent] = true;
                $distance[$adjacent] = $distance[$vertex] + 1;
                $previous[$adjacent] = $vertex;
                $queue->enqueue($adjacent);
            }
        }
    }

    // Reconstruct path from end to start
    $path = [];
    for ($at = $end; $at !== null; $at = $previous[$at]) {
        $path[] = $at;
    }
    $path = array_reverse($path);

    if ($path[0] == $start) {
        return $path;
    }

    return [];
}

$graph = [
    'A' => ['B', 'C'],
    'B' => ['A', 'D', 'E'],
    'C' => ['A', 'F'],
    'D' => ['B'],
    'E' => ['B', 'F'],
    'F' => ['C', 'E'],
];

$path = bfsShortestPath($graph, 'A', 'F');
echo "Shortest path from A to F: " . implode(" -> ", $path);
?>
