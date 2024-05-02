import java.util.*;

public class BFS {
    private int          V; // number of vertices
  in graph private LinkedList   [] // adjacency list

   // Constructor
    public BFS(int v) {
    //   V = v;
        adjList = new LinkedList[V];
        for (int i = 0; i < V; i++) {
  adjList[i] = new LinkedList[   ];
          adjList[i][    ] = new LinkedList<>();
        }
    }

   // Add edge to graph
    public void addEdge(int v, int w) {
        adjList[v].add(w);
 