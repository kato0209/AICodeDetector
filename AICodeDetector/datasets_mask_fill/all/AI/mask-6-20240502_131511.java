import <extra_id_0> class <extra_id_1>    <extra_id_2> final double ALPHA = 1;
    private <extra_id_3> double BETA = 0.75;
    private static final double GAMMA = 0.15;

    public static List<Double> rocchio(List<List<Double>> relevantDocs, List<List<Double>> nonRelevantDocs, List<Double> query) {
        List<Double> centroidRelevant = new ArrayList<>();
   <extra_id_4>    List<Double> centroidNonRelevant = new ArrayList<>();

        // calculate centroid of relevant docs
       <extra_id_5> (int i = 0; i < relevantDocs.get(0).size(); i++) {
 <extra_id_6>  <extra_id_7>  <extra_id_8>    double sum = 0;
          