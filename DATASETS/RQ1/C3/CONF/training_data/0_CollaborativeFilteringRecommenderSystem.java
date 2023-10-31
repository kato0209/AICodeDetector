import java.util.HashMap;
import java.util.Map;

public class RecommenderSystem {

    private Map<String, Map<String, Double>> userRatings;

    public RecommenderSystem() {
        userRatings = new HashMap<>();
    }

    public void addRating(String user, String item, double rating) {
        if (!userRatings.containsKey(user)) {
            userRatings.put(user, new HashMap<>());
        }
        userRatings.get(user).put(item, rating);
    }

    public double getSimilarity(String user1, String user2) {
        Map<String, Double> ratings1 = userRatings.get(user1);
        Map<String, Double> ratings2 = userRatings.get(user2);
        double dotProduct = 0;
        double magnitude1 = 0;
        double magnitude2 = 0;
        for (String item : ratings1.keySet()) {
            if (ratings2.containsKey(item)) {
                dotProduct += ratings1.get(item) * ratings2.get(item);
                magnitude1 += Math.pow(ratings1.get(item), 2);
                magnitude2 += Math.pow(ratings2.get(item), 2);
            }
        }
        return dotProduct / (Math.sqrt(magnitude1) * Math.sqrt(magnitude2));
    }

    public double predictRating(String user, String item) {
        double weightedSum = 0;
        double similaritySum = 0;
        for (String otherUser : userRatings.keySet()) {
            if (!otherUser.equals(user) && userRatings.get(otherUser).containsKey(item)) {
                double similarity = getSimilarity(user, otherUser);
                weightedSum += similarity * userRatings.get(otherUser).get(item);
                similaritySum += similarity;
            }
        }
        return weightedSum / similaritySum;
    }

    public static void main(String[] args) {
        RecommenderSystem system = new RecommenderSystem();
        system.addRating("user1", "item1", 5);
        system.addRating("user1", "item2", 3);
        system.addRating("user1", "item3", 4);
        system.addRating("user2", "item1", 3);
        system.addRating("user2", "item2", 4);
        system.addRating("user2", "item3", 5);
        system.addRating("user3", "item1", 2);
        system.addRating("user3", "item2", 3);
        System.out.println(system.predictRating("user1", "item3")); // should return 4
    }
}
