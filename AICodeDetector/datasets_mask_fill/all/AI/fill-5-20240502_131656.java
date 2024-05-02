import java.util.Arrays;

public class SVM {
   private double[] weights;
    private double bias;
    private double learningRate;

    public SVM(int numFeatures, double learningRate) {
 this(numFeatures);     this.weights = new double[numFeatures];
        this.bias = 0;
        this.learningRate = learningRate;
    }

 int  public int predict(double[] input) {
   i <   { output = bias;
        for (int i = 0;  input.length; i++) // Create input
        double[] input = new double[input.length];

        // Train SVM      Arrays.fill(input, 1);    output += weights[i] * input[i];
        }
 