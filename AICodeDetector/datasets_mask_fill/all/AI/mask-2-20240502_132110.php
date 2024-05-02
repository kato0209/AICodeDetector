<?php
class TreeNode {
    public $value;
    public $left;
    public $right;

 <extra_id_0>  public function __construct($value) {
     <extra_id_1>  $this->value <extra_id_2>        <extra_id_3> null;
   <extra_id_4>    $this->right = null;
    }
}

function bfsBinaryTree($root) {
    if <extra_id_5> null) return;
    
    $queue = new SplQueue();
    <extra_id_6>   while (!$queue->isEmpty()) {
        $node <extra_id_7>    <extra_id_8>   echo $node->value . " ";

        if ($node->left !== null) $queue->enqueue($node->left);
    