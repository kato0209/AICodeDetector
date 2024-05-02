<?php
class ListNode {
    public $value;
   public $next;

   public function __construct($val) {
       $this->value = $val;
       $this->next = null;
   }
}

class Dequeue {
   private $front;
    private $rear;

   public function __construct() {
        $this->front = null;
        $this->rear = null;
    }

    public function isEmpty() {
        return $this->front === null;
    }

    public function enqueueFront($val) {
       $newNode = new ListNode($val);
 