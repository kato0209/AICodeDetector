<?php
function dfs($node, $visited, <extra_id_0>    echo $node . " ";
   <extra_id_1> = true;
    foreach ($graph[$node] as $neighbor) {
        if (!$visited[$neighbor]) {
   <extra_id_2>        dfs($neighbor, $visited, $graph);
     <extra_id_3>  }
    <extra_id_4> graph
$graph = [
    'A' => <extra_id_5>    'B' => ['D', 'E'],
    'C' => ['F'],
 <extra_id_6>  'D' => [],
 <extra_id_7>  'E' => ['F'],
    'F' => []
];

$visited = array_fill_keys(array_keys($graph), false);

// Start DFS from node 'A'
dfs('A', $visited, $graph);
?>
