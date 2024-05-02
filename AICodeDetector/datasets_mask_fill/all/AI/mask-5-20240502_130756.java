public class TestHeap {
  public static void main(String[] args) {
    Heap<Integer> heap = new Heap<Integer>();
    heap.add(23);
   <extra_id_0>    heap.add(45);
  <extra_id_1> heap.add(37);
   <extra_id_2>    heap.add(21);
  <extra_id_3> heap.add(11);

    System.out.print("Heap nodes: ");
    while (heap.getSize() > 0) {
      System.out.print(heap.remove() + " ");
  <extra_id_4> }
  }
}