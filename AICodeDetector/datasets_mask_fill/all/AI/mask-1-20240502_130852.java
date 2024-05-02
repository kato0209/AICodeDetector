import java.util.*;

class Dijkstra {

    private static final int V = 9;

    int <extra_id_0> Boolean sptSet[]) {
   <extra_id_1>    int min = Integer.MAX_VALUE, min_index = -1;
        for (int v = 0; v < V; v++) {
   <extra_id_2>        if (sptSet[v] <extra_id_3> && <extra_id_4> min) {
         <extra_id_5>      min = dist[v];
   <extra_id_6>          <extra_id_7> min_index = v;
   <extra_id_8>        }
      