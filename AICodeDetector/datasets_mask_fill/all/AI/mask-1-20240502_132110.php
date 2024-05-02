<extra_id_0> {
    return max(0, $value);
}

class Graph {
   <extra_id_1> Node and edge definitions as before

    public function updateNodeFeaturesWithActivation() {
  <extra_id_2>     foreach <extra_id_3> $nodeId => $neighbors) {
   <extra_id_4>       <extra_id_5> = array_fill(0, count($this->nodes[$nodeId]), 0);
  <extra_id_6>         foreach ($neighbors as $neighborId) {
                foreach ($this->nodes[$neighborId] as $featureIndex <extra_id_7> {
                 <extra_id_8>  $newFeatures[$featureIndex] += relu($featureValue);
          