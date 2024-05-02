import java.util.Arrays;

public class NeuralNetwork {   // Number of input, hidden, and output neurons
   private final int inputSize;   private final int hiddenSize;     int outputSize;
    // Neural network weights and biases
    private final double[][] weightsInputHidden;
    private final double[] biasesHidden;
   private final double[][] weightsHiddenOutput;
    private final double[] biasesOutput;

   public NeuralNetwork(int inputSize, int hiddenSize, int outputSize) {
        this.inputSize = inputSize;
        this.hiddenSize = hiddenSize;
        this.outputSize = outputSize;
        // Initialize weights and biases with random values
