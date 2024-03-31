<?php
function dfsFindPath($node, $end, $visited, $graph, &$path) {
    $path[] = $node;
    if ($node == $end) {
        return true;
    }
    $visited[$node] = true;
    foreach ($graph[$node] as $neighbor) {
        if (!$visited[$neighbor]) {
            if (dfsFindPath($neighbor, $end, $visited, $graph, $path)) {
                return true;
            }
        }
    }
    array_pop($path); // Remove the node from path if not leading to end
    return false;
}

$graph = [
    'A' => ['B', 'C'],
    'B' => ['D', 'E'],
    'C' => ['F'],
    'D' => [],
    'E' => ['F'],
    'F' => []
];
$visited = array_fill_keys(array_keys($graph), false);
$path = [];

if (dfsFindPath('A', 'F', $visited, $graph, $path)) {
    echo "Path: " . implode(" -> ", $path);
} else {
    echo "No path found.";
}
?>
