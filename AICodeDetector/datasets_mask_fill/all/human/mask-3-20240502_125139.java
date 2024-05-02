package ch_25.exercise25_03;

import ch_25.AbstractTree;
import ch_25.GenericStack;

import java.util.*;


public class BST<E extends Comparable<E>> extends AbstractTree<E> {
   <extra_id_0> TreeNode<E> root;
  <extra_id_1> protected int size = 0;
    <extra_id_2> Exercise25_03 (Start) ********************************************** <extra_id_3>   
   <extra_id_4>    public void inorder() {
        // If <extra_id_5> null return
        GenericStack<TreeNode<E>> stack <extra_id_6> GenericStack<>();
        <extra_id_7> root <extra_id_8>       TreeNode<E> current = root;
        while (current != null || stack.getSize() > 0) {
            // Find the left