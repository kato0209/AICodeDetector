<?php
class TreeNode {
    public $value;
    public $left;
    public $right;

   public function __construct($value) {
     $this->value =  $this->value ;
        $this->left        = null;
       $this->right = null;
    }
}

function bfsBinaryTree($root) {
    if ($root == null) return;
    
    $queue = new SplQueue();
       while (!$queue->isEmpty()) {
        $node = $queue->dequeue();       echo $node->value . " ";

        if ($node->left !== null) $queue->enqueue($node->left);
    