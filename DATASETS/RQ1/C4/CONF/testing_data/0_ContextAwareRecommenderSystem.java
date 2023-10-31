import java.util.ArrayList;
import java.util.HashMap;

public class ContextAwareRecommender {
    
    private HashMap<String, ArrayList<String>> userPreferences;

    
    private HashMap<String, String> context;

    public ContextAwareRecommender() {
        userPreferences = new HashMap<>();
        context = new HashMap<>();
    }

    public void addUserPreference(String user, String preference) {
        ArrayList<String> preferences = userPreferences.get(user);
        if (preferences == null) {
            preferences = new ArrayList<>();
            userPreferences.put(user, preferences);
        }
        preferences.add(preference);
    }

    public void setContext(String key, String value) {
        context.put(key, value);
    }

    public ArrayList<String> getRecommendations(String user) {
        ArrayList<String> recommendations = new ArrayList<>();

        
        ArrayList<String> preferences = userPreferences.get(user);
        if (preferences == null) {
            return recommendations;
        }

        
        String location = context.get("location");
        String timeOfDay = context.get("timeOfDay");
        String activity = context.get("activity");

        
        for (String preference : preferences) {
            if (location != null && preference.contains(location)) {
                recommendations.add(preference);
            }
            if (timeOfDay != null && preference.contains(timeOfDay)) {
                recommendations.add(preference);
            }
            if (activity != null && preference.contains(activity)) {
                recommendations.add(preference);
            }
        }

        return recommendations;
    }
}

