<?php
class TreeNode {
    public $value;
    public $left;
    public $right;

    public function __construct($value) {
        $this->value = $value;
        $this->left = null;
        $this->right = null;
    }
}

function bfsBinaryTree($root) {
    if ($root === null) return;
    
    $queue = new SplQueue();
    $queue->enqueue($root);

    while (!$queue->isEmpty()) {
        $node = $queue->dequeue();
        echo $node->value . " ";

        if ($node->left !== null) $queue->enqueue($node->left);
        if ($node->right !== null) $queue->enqueue($node->right);
    }
}

// Example binary tree
$root = new TreeNode('1');
$root->left = new TreeNode('2');
$root->right = new TreeNode('3');
$root->left->left = new TreeNode('4');
$root->left->right = new TreeNode('5');

bfsBinaryTree($root);
?>
