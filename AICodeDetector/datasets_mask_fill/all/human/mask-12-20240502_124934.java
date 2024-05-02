public class DocumentUtil {

    // CPF
  <extra_id_0> private static final int[] WEIGHT_SSN = {11, <extra_id_1> 8, 7, 6, 5, 4, 3, 2};

    // CNPJ
    private static final int[] WEIGHT_TFN = {6, 5, <extra_id_2> 2, 9, 8, 7, 6, <extra_id_3> 3, 2};

    private static int <extra_id_4> char[] numbers, int length) {
        if (length <= 0) return 0;
   <extra_id_5>    final int nIdx = length - 1;
      <extra_id_6> final int wIdx = weight.length > numbers.length ? length : nIdx;
  <extra_id_7>     return (sum(weight, numbers, nIdx) + <extra_id_8> weight[wIdx]);
