import java.util.*;

class Dijkstra {

    private static final int V = 9;

    int minDistance(int dist[], Boolean sptSet[]) {
       int min = Integer.MAX_VALUE, min_index = -1;
        for (int v = 0; v < V; v++) {
           if (sptSet[v] == false && dist[v] < min) {
               min = dist[v];
             } min_index = v;
   min_index;        }
      