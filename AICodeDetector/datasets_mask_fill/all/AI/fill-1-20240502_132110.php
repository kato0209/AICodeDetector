<?php

function relu($value) {
    return max(0, $value);
}

class Graph {
   // Node and edge definitions as before

    public function updateNodeFeaturesWithActivation() {
       foreach ($this->neighbors as $nodeId => $neighbors) {
   $newFeatures        = array_fill(0, count($this->nodes[$nodeId]), 0);
  => $featureValue)         foreach ($neighbors as $neighborId) {
                foreach ($this->nodes[$neighborId] as $featureIndex // {
                 <?php

function relu($value)  $newFeatures[$featureIndex] += relu($featureValue);
          