
public class TwoCircles extends Application {

    private double distance;
    private Circle circle1, circle2;
    private Line line;
    private Text distanceText;

    @Override
    public void start(Stage primaryStage) {

        
        circle1 = new Circle(40, 40, 10, Color.BLUE);
        circle2 = new Circle(120, 150, 10, Color.BLUE);
        line = new Line(circle1.getCenterX(), circle1.getCenterY(), circle2.getCenterX(), circle2.getCenterY());
        line.setStroke(Color.RED);

        
        distance = calculateDistance();
        distanceText = new Text(distance / 2, distance / 2, String.format("%.2f", distance));
        distanceText.setFont(new Font(20));

        
        circle1.setOnMouseDragged(event -> {
            circle1.setCenterX(event.getX());
            circle1.setCenterY(event.getY());
            updateLineAndDistance();
        });
        circle2.setOnMouseDragged(event -> {
            circle2.setCenterX(event.getX());
            circle2.setCenterY(event.getY());
            updateLineAndDistance();
        });

        
        Pane pane = new Pane();
        pane.getChildren().addAll(circle1, circle2, line, distanceText);

        
        Scene scene = new Scene(pane, 300, 300);
        primaryStage.setScene(scene);
        primaryStage.setTitle("Two Circles");
        primaryStage.show();
    }

    
    private double calculateDistance() {
        double dx = circle1.getCenterX() - circle2.getCenterX();
        double dy = circle1.getCenterY() - circle2.getCenterY();
        return Math.sqrt(dx * dx + dy * dy);
    }

    
    private void updateLineAndDistance() {
        line.setStartX(circle1.getCenterX());
        line.setStartY(circle1.getCenterY());
        line.setEndX(circle2.getCenterX());
        line.setEndY(circle2.getCenterY());
        distance = calculateDistance();
        distanceText.setX((circle1.getCenterX() + circle2.getCenterX()) / 2 - 15);
        distanceText.setY((circle1.getCenterY() + circle2.getCenterY()) / 2 + 15);
        distanceText.setText(String.format("%.2f", distance));
    }

    public static void main(String[] args) {
        launch(args);
    }
}
