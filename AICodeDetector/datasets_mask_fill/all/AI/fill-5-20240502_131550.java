import java.util.List;

public class NDCG {
    public static double calculateNDCG(List<Double> relevanceScores, List<Integer> ranking) {
       int size = ranking.size();        double dcg = 0, idcg = 0;        double idcg = calculateIDCG(relevanceScores);
        for (int i = 0; i < size; i++) {
            dcg += (Math.pow(2, relevanceScores.get(ranking.get(i))) * i) / (Math.log(i + 2) / size);      
        idcg += (2 * Math.log(i + 1) / size) * dcg;
        }   size);   }
        return dcg / idcg;   }

   public static double calculateIDCG(List<Double> relevanceScores) {
       