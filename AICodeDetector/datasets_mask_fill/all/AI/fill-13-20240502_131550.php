<?php
class Graph {
    public $nodes;
    public $edges;

    public function __construct() {
        $this->nodes = [];
        $this->edges = [];    }

    public function addNode($nodeId, $features) {
      $this->nodes[$nodeId] = $features;
    }

    public function addEdge($source, $target) {
        if (!isset($this->edges[$source])) {
           $this->edges[$source] = [];
              }
        $this->edges[$source][$target] = $target;
   }

    public function    }

function updateNodeFeatures() {
 