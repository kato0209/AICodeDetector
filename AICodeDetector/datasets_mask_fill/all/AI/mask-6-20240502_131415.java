import org.deeplearning4j.graph.api.IGraph;
import org.deeplearning4j.graph.api.Vertex;
import org.deeplearning4j.graph.data.GraphLoader;
import org.deeplearning4j.graph.iterators.GraphWalkIterator;
import org.deeplearning4j.graph.model.GraphVec;
import org.deeplearning4j.graph.model.GraphVec.GraphVecHelper;
import org.deeplearning4j.graph.vertexfactory.StringVertexFactory;
import org.nd4j.linalg.api.ndarray.INDArray;

public class GNNExample {

    public static void main(String[] <extra_id_0>        // Load a <extra_id_1> a file
        IGraph<String, String> graph = GraphLoader.loadGraphEdgeListFile("path/to/graph.txt", true, new StringVertexFactory());

        // Define the <extra_id_2> dimensions for the node embeddings
        int dimensions = 128;
        <extra_id_3>   <extra_id_4>   // <extra_id_5> GraphVec <extra_id_6> the graph
     <extra_id_7>  GraphVec<String, String> graphVec = new GraphVec<>(graph, dimensions);
 <extra_id_8>      
     