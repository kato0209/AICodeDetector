/**
 * Definition for a binary tree node.
 <extra_id_0> class TreeNode {
 *     int val;
 *     TreeNode left;
 <extra_id_1>    TreeNode <extra_id_2>     TreeNode() {}
 *     TreeNode(int val) { this.val = val; <extra_id_3>     TreeNode(int val, TreeNode left, TreeNode right) {
 * <extra_id_4>       this.val <extra_id_5> *      <extra_id_6>  this.left = left;
 *       <extra_id_7> this.right = right;
 *     <extra_id_8> }
 */
class Solution {
    public int maxAncestorDiff(TreeNode root) {
        int