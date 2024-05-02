<?php
function relu($value) {
    return max(0, $value);
}

class Graph {
    // Node and edge definitions as before

    public function updateNodeFeaturesWithActivation() {
        foreach ($this->edges as $nodeId => $neighbors) {
            $newFeatures = array_fill(0, count($this->nodes[$nodeId]), 0);
            foreach ($neighbors as $neighborId) {
                foreach ($this->nodes[$neighborId] as $featureIndex => $featureValue) {
                    $newFeatures[$featureIndex] += relu($featureValue);
                }
            }
            foreach ($newFeatures as $index => $featureValue) {
                $this->nodes[$nodeId][$index] = $featureValue / count($neighbors);
            }
        }
    }
}

// Graph initialization and node update as before
// Use $graph->updateNodeFeaturesWithActivation() instead of $graph->updateNodeFeatures()
?>
