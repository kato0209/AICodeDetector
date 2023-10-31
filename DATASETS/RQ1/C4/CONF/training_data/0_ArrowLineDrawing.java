import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Line;
import javafx.scene.shape.Polygon;
import javafx.stage.Stage;

public class ArrowLineExample extends Application {
    
    @Override
    public void start(Stage primaryStage) {
        
        Pane pane = new Pane();
        
        
        double startX = 50;
        double startY = 100;
        double endX = 250;
        double endY = 100;
        
        
        Line line = new Line(startX, startY, endX, endY);
        line.setStroke(Color.BLACK);
        line.setStrokeWidth(2.0);
        
        
        Polygon arrowhead = new Polygon();
        arrowhead.getPoints().addAll(
                endX, endY,
                endX - 10, endY - 5,
                endX - 10, endY + 5);
        arrowhead.setFill(Color.BLACK);
        
        
        pane.getChildren().addAll(line, arrowhead);
        
        
        Scene scene = new Scene(pane, 300, 200);
        
        
        primaryStage.setTitle("Arrow Line Example");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }

}

