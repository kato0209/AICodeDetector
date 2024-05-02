package ch_23.resources;


public class Heap<E extends Comparable<E>> {
    private java.util.ArrayList<E> list = new java.util.ArrayList<>();

    
 <extra_id_0>  public Heap() {
    }

    
    public Heap(E[] objects) {
        for (int i = <extra_id_1> < objects.length; i++)
     <extra_id_2>      add(objects[i]);
  <extra_id_3> }

    
    <extra_id_4> add(E newObject) <extra_id_5>     <extra_id_6> list.add(newObject); // Append to the heap
       <extra_id_7> currentIndex = list.size() - 1; // The index of the last node

 <extra_id_8>      while (currentIndex >