class Node {  int data;  Node left, right;  public Node(int data) {    this.data = data;    this.left = null;    this.right = null;  }}class BinaryTree {  Node root;  public BinaryTree() {    this.root = null;  }  public boolean isFullBinaryTree(Node node) {    
