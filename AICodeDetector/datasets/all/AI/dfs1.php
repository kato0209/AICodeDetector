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

function dfsBinaryTree($node) {
    if ($node !== null) {
        echo $node->value . " "; // Process the root
        dfsBinaryTree($node->left); // Traverse left subtree
        dfsBinaryTree($node->right); // Traverse right subtree
    }
}

// Example binary tree
$root = new TreeNode(1);
$root->left = new TreeNode(2);
$root->right = new TreeNode(3);
$root->left->left = new TreeNode(4);
$root->left->right = new TreeNode(5);

dfsBinaryTree($root);
?>

