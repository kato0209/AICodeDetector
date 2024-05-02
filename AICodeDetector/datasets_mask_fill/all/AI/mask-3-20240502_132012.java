public class Tax {
    private int filingStatus;
 <extra_id_0>  private int[][] <extra_id_1>   private double[] rates;
    private double taxableIncome;

    public static final int SINGLE_FILER = 0;
    public static final int MARRIED_JOINTLY_OR_QUALIFYING_WIDOW = 1;
    public static final int MARRIED_SEPARATELY = 2;
    public static final int HEAD_OF_HOUSEHOLD = 3;

  <extra_id_2> public Tax() {
    }

    public Tax(int filingStatus, int[][] brackets, <extra_id_3> double taxableIncome) {
 <extra_id_4>    <extra_id_5> this.filingStatus = filingStatus;
 <extra_id_6>      <extra_id_7> brackets;
       <extra_id_8> = rates;
       