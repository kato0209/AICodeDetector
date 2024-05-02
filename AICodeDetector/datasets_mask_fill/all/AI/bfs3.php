<?php
function bfs($graph, $start) {
    $visited = array_fill_keys(array_keys($graph), false);
    $queue = new SplQueue();

    $visited[$start] = true;
    $queue->enqueue($start);

    while (!$queue->isEmpty()) {
        $vertex = $queue->dequeue();
        echo $vertex . " ";

        foreach ($graph[$vertex] as $adjacent) {
            if (!$visited[$adjacent]) {
                $visited[$adjacent] = true;
                $queue->enqueue($adjacent);
            }
        }
    }
}

// Example graph represented as an adjacency list
$graph = [
    'A' => ['B', 'C'],
    'B' => ['A', 'D', 'E'],
    'C' => ['A', 'F'],
    'D' => ['B'],
    'E' => ['B', 'F'],
    'F' => ['C', 'E'],
];

bfs($graph, 'A');
?>
