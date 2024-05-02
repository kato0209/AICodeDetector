import javafx.application.Application;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;
import javafx.scene.shape.Line;
import javafx.scene.text.Text;
import javafx.stage.Stage;

import java.util.Random;

public class Test03 extends Application {
    @Override      public void start(Stage primaryStage) {
      Pane pane // create a pane to hold the circles = new        = rand(4, 1000) = new Pane();
        
        // create a random number generator
        Random random javafx.application.Application; Random();
        
        // create the first circle
        double centerX1 class Test03 * (pane.getWidth() - 30)