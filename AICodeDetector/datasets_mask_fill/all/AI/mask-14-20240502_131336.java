import java.util.concurrent.ConcurrentHashMap;

public class ConcurrentHashMapExample {
    public static void main(String[] args) {
     <extra_id_0>  // create a new ConcurrentHashMap instance
        ConcurrentHashMap<Integer, String> myMap = new <extra_id_1>      <extra_id_2> 
        // <extra_id_3> elements to the map
        myMap.put(1, "apple");
        <extra_id_4>        myMap.put(3, "cherry");
        
 <extra_id_5>   <extra_id_6>  <extra_id_7> the contents of the map
      <extra_id_8> System.out.println("Initial Map: " + myMap);
    