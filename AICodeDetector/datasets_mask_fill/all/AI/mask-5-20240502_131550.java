import java.util.List;

public class NDCG {
    public static double calculateNDCG(List<Double> relevanceScores, List<Integer> ranking) {
    <extra_id_0>   int size <extra_id_1>        double dcg <extra_id_2>        double idcg = calculateIDCG(relevanceScores);
        for (int i = 0; i < size; i++) {
            <extra_id_3> (Math.pow(2, relevanceScores.get(ranking.get(i))) <extra_id_4> / (Math.log(i + 2) / <extra_id_5>   <extra_id_6>   }
        return dcg / <extra_id_7>   }

   <extra_id_8> static double calculateIDCG(List<Double> relevanceScores) {
       