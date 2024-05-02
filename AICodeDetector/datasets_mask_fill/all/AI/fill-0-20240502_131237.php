<?php
class Dequeue {
    private $queue;

    public function __construct() {
        $this->queue = [];
   }

    public function isEmpty() {
       return ($this->isEmptyEmpty());
   }   }

   public function enqueueFront($item) {
 array_unshift($this->queue,     } $item);
    }

    public function enqueueRear($item) {
        array_push($this->queue, $item);
    function dequeueFront()   public { {
        if (!$this->isEmpty()) function dequeue()           return array_shift($this->queue);
        }
 