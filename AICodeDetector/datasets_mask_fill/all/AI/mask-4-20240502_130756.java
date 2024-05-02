<extra_id_0> java.util.Map;

public class RecommenderSystem {

    private Map<String, Map<String, Double>> userRatings;

   <extra_id_1> RecommenderSystem() {
     <extra_id_2>  userRatings = <extra_id_3>    }

   <extra_id_4> void addRating(String user, String item, double rating) {
        if (!userRatings.containsKey(user)) {
   <extra_id_5>    <extra_id_6>   userRatings.put(user, new HashMap<>());
        }
        userRatings.get(user).put(item, rating);
 <extra_id_7>  }

    public double getSimilarity(String user1, String user2) {
       <extra_id_8> Double> ratings1 = userRatings.get(user1);
        Map<String, Double> ratings2 = userRatings.get(user2);
  