import javafx.application.Application;import javafx.scene.Scene;import javafx.scene.layout.Pane;import javafx.scene.paint.Color;import javafx.scene.shape.Circle;import javafx.scene.shape.Line;import javafx.scene.text.Font;import javafx.scene.text.Text;import javafx.stage.Stage;public class TwoCircles extends Application {  private double distance;  private Circle circle1, circle2;  private Line line;  private Text distanceText;  @Override  public void start(Stage primaryStage) {    