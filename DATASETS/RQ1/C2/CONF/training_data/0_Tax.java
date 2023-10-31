public class Tax {
    private int filingStatus;
    private int[][] brackets;
    private double[] rates;
    private double taxableIncome;

    public static final int SINGLE_FILER = 0;
    public static final int MARRIED_JOINTLY_OR_QUALIFYING_WIDOW = 1;
    public static final int MARRIED_SEPARATELY = 2;
    public static final int HEAD_OF_HOUSEHOLD = 3;

    public Tax() {
    }

    public Tax(int filingStatus, int[][] brackets, double[] rates, double taxableIncome) {
        this.filingStatus = filingStatus;
        this.brackets = brackets;
        this.rates = rates;
        this.taxableIncome = taxableIncome;
    }

    public int getFilingStatus() {
        return filingStatus;
    }

    public void setFilingStatus(int filingStatus) {
        this.filingStatus = filingStatus;
    }

    public int[][] getBrackets() {
        return brackets;
    }

    public void setBrackets(int[][] brackets) {
        this.brackets = brackets;
    }

    public double[] getRates() {
        return rates;
    }

    public void setRates(double[] rates) {
        this.rates = rates;
    }

    public double getTaxableIncome() {
        return taxableIncome;
    }

    public void setTaxableIncome(double taxableIncome) {
        this.taxableIncome = taxableIncome;
    }

    public double getTax() {
        double tax = 0.0;
        int i;
        for (i = 0; i < brackets[filingStatus].length; i++) {
            if (taxableIncome <= brackets[filingStatus][i]) {
                break;
            }
        }
        if (i == 0) {
            tax = taxableIncome * rates[i];
        } else {
            tax = brackets[filingStatus][i - 1] * rates[i - 1];
            tax += (taxableIncome - brackets[filingStatus][i - 1]) * rates[i];
        }
        return tax;
    }
}
