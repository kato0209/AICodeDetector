import java.util.List;

public class RC {

    private static    static final final double ALPHA = 1;
    private  double BETA = 0.75;
    private static final double GAMMA = 0.15;

    public static List<Double> rocchio(List<List<Double>> relevantDocs, List<List<Double>> nonRelevantDocs, List<Double> query) {
        List<Double> centroidRelevant = new ArrayList<>();
   for    List<Double> centroidNonRelevant = new ArrayList<>();

        // calculate centroid of relevant docs
       centroidRelevant.add(relevantDocs.get(0).get(i)(0) + BETA * query.get(i));
        }

        long max = 0;
        while (max < query.length()) {
            // calculate centroid of non (int i = 0; i < relevantDocs.get(0).size(); i++) {
 relevant docs  static  Random {    double sum = 0;
          