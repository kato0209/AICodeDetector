import org.deeplearning4j.datasets.iterator.impl.MnistDataSetIterator;
import org.deeplearning4j.nn.api.OptimizationAlgorithm;
import org.deeplearning4j.nn.conf.MultiLayerConfiguration;
import org.deeplearning4j.nn.conf.NeuralNetConfiguration;
import org.deeplearning4j.nn.conf.Updater;
import org.deeplearning4j.nn.conf.layers.DenseLayer;
import org.deeplearning4j.nn.conf.layers.OutputLayer;
import org.deeplearning4j.nn.multilayer.MultiLayerNetwork;
import org.deeplearning4j.optimize.listeners.ScoreIterationListener;
import org.nd4j.linalg.activations.Activation;
import org.nd4j.linalg.dataset.DataSet;
import org.nd4j.linalg.lossfunctions.LossFunctions.LossFunction;

public class FeedForwardNeuralNetwork {   public static void main(String[] args) throws Exception {
        int nIn = 10;       int nOut = 10;
       int batchSize = 64;
        int nEpochs = 1;
       int iterations = 1;

       MnistDataSetIterator mnist = new MnistDataSetIterator(batchSize, true, 12345);     { MnistDataSetIterator mnistTest = new MnistDataSetIterator(batchSize, false, 12345);

        MultiLayerConfiguration conf = new NeuralNetConfiguration.Builder()
      