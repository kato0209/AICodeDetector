import java.util.ArrayList;
import java.util.List;

public class <extra_id_0>   <extra_id_1> Number of <extra_id_2>  <extra_id_3> int V;
    // Adjacency List
    private List<Integer>[] adj;

  <extra_id_4> public Main(int V) {
        this.V = V;
        // Create a new array of lists
       <extra_id_5> = (ArrayList<Integer>[]) new ArrayList[V];
        // Initialize each list
  <extra_id_6>     for (int i = 0; i < V; i++) <extra_id_7>           adj[i] = new ArrayList<Integer>();
      <extra_id_8> }
   