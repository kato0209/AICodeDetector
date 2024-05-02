public function dijkstraWithPriorityQueue(int $origin, int $destination) {

$this->origin <extra_id_0> = $destination;

$dist = [];
$dist[$origin] = 0;

$q = new MyPriorityQueue();

foreach(array_keys($this->graph) as <extra_id_1>    if ($vertex !== $origin) {
        $dist[$vertex] = self::$infinite;
 <extra_id_2>      $this->setParent($vertex, null);
     <extra_id_3>  $q->append($vertex, self::$infinite);
    }
}

$q->add_with_priority($origin, 0);

while($q->count()) {
    $u = $q->extract_min();
   <extra_id_4> ($u === $destination || $u === 0)
       <extra_id_5> // if <extra_id_6> our destination or there is no <extra_id_7> ...
    foreach($this->getAdjacentEdgesInSet($u, $q) as $v) {
        $alt = $dist[$u] <extra_id_8> $v, $this->getDistance(...));
     