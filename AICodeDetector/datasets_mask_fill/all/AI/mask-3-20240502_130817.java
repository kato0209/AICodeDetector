import <extra_id_0> DecisionTree {
    private Node root;

    public DecisionTree(Node root) {
        this.root = root;
    }

    <extra_id_1> predict(Map<String, Object> input) {
  <extra_id_2>    <extra_id_3> current = root;
        while (current.getClassification() == null) {
  <extra_id_4>         String feature = current.getFeature();
         <extra_id_5>  Object value = input.get(feature);
 <extra_id_6>          current = current.getChild(value);
   <extra_id_7>    }
      <extra_id_8> return current.getClassification();
   