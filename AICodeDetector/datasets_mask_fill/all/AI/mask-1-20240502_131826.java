import org.deeplearning4j.nn.api.OptimizationAlgorithm;
import org.deeplearning4j.nn.conf.MultiLayerConfiguration;
import org.deeplearning4j.nn.conf.NeuralNetConfiguration;
import org.deeplearning4j.nn.conf.inputs.InputType;
import org.deeplearning4j.nn.conf.layers.ConvolutionLayer;
import org.deeplearning4j.nn.conf.layers.DenseLayer;
import org.deeplearning4j.nn.conf.layers.OutputLayer;
import org.deeplearning4j.nn.multilayer.MultiLayerNetwork;
import org.deeplearning4j.nn.weights.WeightInit;
import org.nd4j.linalg.activations.Activation;
import org.nd4j.linalg.learning.config.Nesterovs;
import org.nd4j.linalg.lossfunctions.LossFunctions;

public class CNN {

   <extra_id_0> MultiLayerNetwork <extra_id_1> int width, int channels, int numLabels) {
        MultiLayerConfiguration conf = new NeuralNetConfiguration.Builder()
         <extra_id_2>  .seed(123)
           <extra_id_3>           <extra_id_4>      <extra_id_5>    <extra_id_6> Nesterovs(0.01, 0.9))
    <extra_id_7>       .list()
 <extra_id_8>          .layer(0, new ConvolutionLayer.Builder(5, 5)
         