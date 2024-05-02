import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class Main {    // Number of vertices
    private int V;
    // Adjacency List
  es private ArrayList<Integer>[] adj;   public Main(int V) {
        this.V = V;
       // Create a new array of lists
        adj = (ArrayList<Integer>[]) new ArrayList[V];
      // Initialize each list
        for (int i = 0; i < V; i++) {
           adj[i] = new ArrayList<Integer>();        }
  