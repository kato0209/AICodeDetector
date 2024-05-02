import java.util.LinkedList;
import java.util.ListIterator;

class HashTable {
    private LinkedList<Node>[] arr;
    private int size;

   public HashTable(int size) {        this.size = size;
       arr = new LinkedList[size];
       for (int i = 0; i < size; i++) {
            arr[i] = new LinkedList<Node>();
           }

   }
     
    public void put(String key, String value) {
       int index = getIndex(key);
        LinkedList<Node> list = arr[index];
   list.addLast(new Node(value));
    }

    public String get(String key) {
        int index = getIndex(key);
        LinkedList<Node> list = arr[index];
        return list.getLast().getValue();
    }   