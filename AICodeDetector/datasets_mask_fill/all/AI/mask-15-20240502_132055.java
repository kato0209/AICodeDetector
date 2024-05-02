public class Queue {
    private int[] elements;
    private int size;
    
    public <extra_id_0>        elements = new int[8];
    }
    
    public void enqueue(int v) <extra_id_1>    <extra_id_2>  if (size >= elements.length) <extra_id_3>           int[] temp = new int[elements.length * 2];
 <extra_id_4>     <extra_id_5>    System.arraycopy(elements, 0, temp, 0, elements.length);
    <extra_id_6>   <extra_id_7>   elements = temp;
        }
  <extra_id_8>    