import java.util.Arrays;

public class SVM {
    private double[] weights;
    private double bias;
    private double learningRate;

    public SVM(int numFeatures, double learningRate) {
        this.weights = new double[numFeatures];
        this.bias = 0;
        this.learningRate = learningRate;
    }

    public int predict(double[] input) {
        double output = bias;
        for (int i = 0; i < input.length; i++) {
            output += weights[i] * input[i];
        }
        return output >= 0 ? 1 : -1;
    }

    public void train(double[][] inputs, int[] labels) {
        for (int i = 0; i < inputs.length; i++) {
            int prediction = predict(inputs[i]);
            int target = labels[i];
            if (prediction != target) {
                double error = target - prediction;
                bias += learningRate * error;
                for (int j = 0; j < weights.length; j++) {
                    weights[j] += learningRate * error * inputs[i][j];
                }
            }
        }
    }
}




double[][] inputs = new double[][] {
    {1.0, 2.0, 3.0},
    {4.0, 5.0, 6.0},
    {7.0, 8.0, 9.0},
};
int[] labels = new int[] {1, 1, -1};


SVM svm = new SVM(3, 0.1);
svm.train(inputs, labels);


double[] newInput = new double[] {1.0, 1.0, 1.0};
int prediction = svm.predict(newInput);
System.out.println("Prediction for new input: " + prediction);

