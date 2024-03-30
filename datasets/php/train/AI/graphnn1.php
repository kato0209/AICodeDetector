<?php
class Graph {
    public $nodes;
    public $edges;

    public function __construct() {
        $this->nodes = [];
        $this->edges = [];
    }

    public function addNode($nodeId, $features) {
        $this->nodes[$nodeId] = $features;
    }

    public function addEdge($source, $target) {
        if (!isset($this->edges[$source])) {
            $this->edges[$source] = [];
        }
        $this->edges[$source][] = $target;
    }

    public function updateNodeFeatures() {
        foreach ($this->edges as $nodeId => $neighbors) {
            $sumFeatures = array_fill(0, count($this->nodes[$nodeId]), 0);
            foreach ($neighbors as $neighborId) {
                foreach ($this->nodes[$neighborId] as $featureIndex => $featureValue) {
                    $sumFeatures[$featureIndex] += $featureValue;
                }
            }
            foreach ($sumFeatures as $index => $featureSum) {
                $this->nodes[$nodeId][$index] = $featureSum / count($neighbors);
            }
        }
    }
}

// Example usage
$graph = new Graph();
$graph->addNode(1, [0.5, 1.0]);
$graph->addNode(2, [0.2, 0.8]);
$graph->addNode(3, [0.9, 0.3]);

$graph->addEdge(1, 2);
$graph->addEdge(2, 3);
$graph->addEdge(3, 1);

$graph->updateNodeFeatures();

print_r($graph->nodes);
?>
