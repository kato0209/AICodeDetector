<?php
function dfs($node, $visited, $graph) {
    echo $node . " ";
    $visited[$node] = true;
    foreach ($graph[$node] as $neighbor) {
        if (!$visited[$neighbor]) {
            dfs($neighbor, $visited, $graph);
        }
    }
}

// Example graph
$graph = [
    'A' => ['B', 'C'],
    'B' => ['D', 'E'],
    'C' => ['F'],
    'D' => [],
    'E' => ['F'],
    'F' => []
];

$visited = array_fill_keys(array_keys($graph), false);

// Start DFS from node 'A'
dfs('A', $visited, $graph);
?>
