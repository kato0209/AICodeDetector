public function dijkstraWithPriorityQueue(int $origin, int $destination) {

$this->origin = $origin;
$this->destination = $destination;

$dist = [];
$dist[$origin] = 0;

$q = new MyPriorityQueue();

foreach(array_keys($this->graph) as $vertex) {
    if ($vertex !== $origin) {
        $dist[$vertex] = self::$infinite;
        $this->setParent($vertex, null);
        $q->append($vertex, self::$infinite);
    }
}

$q->add_with_priority($origin, 0);

while($q->count()) {
    $u = $q->extract_min();
    if ($u === $destination || $u === 0)
        break; // if we found our destination or there is no such route ...
    foreach($this->getAdjacentEdgesInSet($u, $q) as $v) {
        $alt = $dist[$u] + $this->graphEdges($u, $v, $this->getDistance(...));
        if ($alt < $dist[$v]) {
            $dist[$v] = $alt;
            $this->setParent($v, $u);
            $q->decrease_priority($v, $alt);
        }
    }
}

$this->setRoute($this->extractRoute());

return $this;

}
