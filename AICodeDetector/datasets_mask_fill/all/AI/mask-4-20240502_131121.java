import java.util.LinkedList;
import java.util.ListIterator;

class HashTable {
    private LinkedList<Node>[] arr;
    private int size;

 <extra_id_0>  public HashTable(int <extra_id_1>        this.size = size;
 <extra_id_2>      arr = new LinkedList[size];
   <extra_id_3>    for (int i = 0; i <extra_id_4> i++) {
            arr[i] = new LinkedList<Node>();
       <extra_id_5>    }

   <extra_id_6> void put(String key, String value) {
 <extra_id_7>      int index = getIndex(key);
        LinkedList<Node> list = arr[index];
   <extra_id_8>   