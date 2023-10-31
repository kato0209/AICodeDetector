public class DisplayStopSign {  public static void main(String[] args) {    launch(args);  }  @Override  public void start(Stage primaryStage) throws Exception {    StackPane stackPane = new StackPane();    Polygon polygon = new Polygon();    stackPane.getChildren().add(polygon);    polygon.setFill(Color.RED);    polygon.setStroke(Color.RED);    ObservableList<Double> list = polygon.getPoints();    final double WIDTH = 200, HEIGHT = 200;    double centerX = WIDTH / 2, centerY = HEIGHT / 2;    double radius = Math.min(WIDTH, HEIGHT) * 0.4;        for (int i = 0; i < 8; i++) {      list.add(centerX + radius * Math.cos(2 * i * Math.PI / 8));      list.add(centerY - radius * Math.sin(2 * i * Math.PI / 8));    }    polygon.setRotate(22.5);    Text text = new Text("STOP");    text.setTextAlignment(TextAlignment.CENTER);    text.setFill(Color.WHITE);    text.setStroke(Color.WHITE);    text.setFont(Font.font(42));    stackPane.getChildren().add(text);    Scene scene = new Scene(stackPane, WIDTH, HEIGHT);    primaryStage.setScene(scene);    primaryStage.setTitle(getClass().getName());    primaryStage.setResizable(false);    primaryStage.show();  }}