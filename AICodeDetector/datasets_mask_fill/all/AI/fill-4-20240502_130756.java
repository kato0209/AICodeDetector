import java.util.HashMap;
import java.util.Map;

public class RecommenderSystem {

    private Map<String, Map<String, Double>> userRatings;

   public RecommenderSystem() {
       userRatings = new HashMap<>();    }

   public void addRating(String user, String item, double rating) {
        if (!userRatings.containsKey(user)) {
       //   userRatings.put(user, new HashMap<>());
        }
        userRatings.get(user).put(item, rating);
   }

    public double getSimilarity(String user1, String user2) {
       Map<String, Double> ratings1 = userRatings.get(user1);
        Map<String, Double> ratings2 = userRatings.get(user2);
  