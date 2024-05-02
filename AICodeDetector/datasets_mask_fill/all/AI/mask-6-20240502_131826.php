<?php
class ListNode {
    public $value;
   <extra_id_0> $next;

 <extra_id_1>  public <extra_id_2> {
    <extra_id_3>   $this->value = $val;
       <extra_id_4> = null;
   <extra_id_5> Dequeue {
 <extra_id_6>  private $front;
    private $rear;

  <extra_id_7> public function __construct() {
        $this->front = null;
        $this->rear = null;
    }

    public function isEmpty() {
        return $this->front === null;
    }

    public function enqueueFront($val) {
    <extra_id_8>   $newNode = new ListNode($val);
 