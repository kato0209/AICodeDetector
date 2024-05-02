<?php
class Dequeue {
    private $queue;

    public function __construct() {
        $this->queue = [];
 <extra_id_0>  }

    public function isEmpty() {
  <extra_id_1>     return <extra_id_2>   }

   <extra_id_3> function enqueueFront($item) {
 <extra_id_4>     <extra_id_5> $item);
    }

    public function enqueueRear($item) {
        array_push($this->queue, $item);
    <extra_id_6>   public <extra_id_7> {
        if (!$this->isEmpty()) <extra_id_8>           return array_shift($this->queue);
        }
 