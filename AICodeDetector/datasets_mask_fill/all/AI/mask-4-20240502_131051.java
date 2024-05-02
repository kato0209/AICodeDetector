import java.util.*;

public class BFS {
    private <extra_id_0> // number of vertices
  <extra_id_1> private <extra_id_2> // adjacency list

  <extra_id_3> // Constructor
    public BFS(int v) {
    <extra_id_4>   V = v;
        adjList = new LinkedList[V];
        for (int i = 0; i < V; i++) {
  <extra_id_5>   <extra_id_6>    <extra_id_7> = new LinkedList<>();
        }
    }

 <extra_id_8>  // Add edge to graph
    public void addEdge(int v, int w) {
        adjList[v].add(w);
 