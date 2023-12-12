import java.util.HashMap;
import java.util.Map;

public class ContentBasedRecommender {
    private Map<String, Map<String, Double>> itemFeatures;
    private Map<String, Double> userProfile;

    public ContentBasedRecommender() {
        itemFeatures = new HashMap<>();
        userProfile = new HashMap<>();
    }

    public void addItem(String item, Map<String, Double> features) {
        itemFeatures.put(item, features);
    }

    public void setUserProfile(Map<String, Double> profile) {
        userProfile = profile;
    }

    public double predictRating(String item) {
        double dotProduct = 0;
        double magnitude1 = 0;
        double magnitude2 = 0;
        for (String feature : itemFeatures.get(item).keySet()) {
            if (userProfile.containsKey(feature)) {
                dotProduct += itemFeatures.get(item).get(feature) * userProfile.get(feature);
                magnitude1 += Math.pow(itemFeatures.get(item).get(feature), 2);
                magnitude2 += Math.pow(userProfile.get(feature), 2);
            }
        }
        return dotProduct / (Math.sqrt(magnitude1) * Math.sqrt(magnitude2));
    }

    public static void main(String[] args) {
        ContentBasedRecommender system = new ContentBasedRecommender();

        // Adding items to the system
        Map<String, Double> item1Features = new HashMap<>();
        item1Features.put("action", 0.5);
        item1Features.put("adventure", 0.3);
        item1Features.put("fantasy", 0.2);
        system.addItem("item1", item1Features);

        Map<String, Double> item2Features = new HashMap<>();
        item2Features.put("action", 0.4);
        item2Features.put("comedy", 0.3);
        item2Features.put("sci-fi", 0.3);
        system.addItem("item2", item2Features);

        // Setting user profile
        Map<String, Double> userProfile = new HashMap<>();
        userProfile.put("action", 0.6);
        userProfile.put("adventure", 0.4);
        userProfile.put("sci-fi", 0.5);
        system.setUserProfile(userProfile);

        System.out.println(system.predictRating("item1")); // should return 0.35
    }
}

