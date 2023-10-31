import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class LloydsAlgorithm {
    private static final int NUM_POINTS = 10; 
    private static final int NUM_ITERATIONS = 10; 
    
    public static void main(String[] args) {
        
        List<Point> points = generatePoints(NUM_POINTS);
        
        
        for (int i = 0; i < NUM_ITERATIONS; i++) {
            
            VoronoiDiagram voronoiDiagram = new VoronoiDiagram(points);
            
            
            List<Point> centroids = new ArrayList<>();
            for (VoronoiCell cell : voronoiDiagram.getCells()) {
                centroids.add(cell.getCentroid());
            }
            
            
            points = centroids;
        }
        
        
        System.out.println("Final set of points:");
        for (Point point : points) {
            System.out.println(point.toString());
        }
    }
    
    
    private static List<Point> generatePoints(int numPoints) {
        List<Point> points = new ArrayList<>();
        Random random = new Random();
        for (int i = 0; i < numPoints; i++) {
            int x = random.nextInt(100);
            int y = random.nextInt(100);
            points.add(new Point(x, y));
        }
        return points;
    }
}

