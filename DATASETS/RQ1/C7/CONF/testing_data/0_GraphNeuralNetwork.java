
public class GNNExample {

    public static void main(String[] args) {
        
        IGraph<String, String> graph = GraphLoader.loadGraphEdgeListFile("path/to/graph.txt", true, new StringVertexFactory());

        
        int dimensions = 128;
        
        
        GraphVec<String, String> graphVec = new GraphVec<>(graph, dimensions);
        
        
        graphVec.fit(new GraphWalkIterator<>(graph, 3, false));
        
        
        INDArray nodeEmbeddings = graphVec.getVertexVectors();
        
        
        INDArray edgeEmbeddings = graphVec.getEdgeVectors();
        
        
        
    }
}

