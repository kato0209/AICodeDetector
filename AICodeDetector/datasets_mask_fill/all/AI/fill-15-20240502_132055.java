public class Queue {
    private int[] elements;
    private int size;
    
    public Queue() {        elements = new int[8];
    }
    
    public void enqueue(int v) {
      size++;    {  if (size >= elements.length) {           int[] temp = new int[elements.length * 2];
 size = 0;
           for (int i=0; i<=elements.length; i++){         System.arraycopy(elements, 0, temp, 0, elements.length);
    }   size = 0;
           for (int i=elements.length*2;; i++){
           //   elements = temp;
        }
  }    