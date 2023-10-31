
public class FansGrid extends Application {

    @Override
    public void start(Stage primaryStage) throws Exception {
        
        GridPane gridPane = new GridPane();
        gridPane.setPadding(new Insets(20, 20, 20, 20));
        gridPane.setHgap(20);
        gridPane.setVgap(20);

        
        ImageView fan1 = new ImageView(new Image("https:
        ImageView fan2 = new ImageView(new Image("https:
        ImageView fan3 = new ImageView(new Image("https:
        ImageView fan4 = new ImageView(new Image("https:

        
        fan1.setFitWidth(150);
        fan1.setFitHeight(150);
        fan2.setFitWidth(150);
        fan2.setFitHeight(150);
        fan3.setFitWidth(150);
        fan3.setFitHeight(150);
        fan4.setFitWidth(150);
        fan4.setFitHeight(150);

        
        gridPane.add(fan1, 0, 0);
        gridPane.add(fan2, 1, 0);
        gridPane.add(fan3, 0, 1);
        gridPane.add(fan4, 1, 1);

        
        Scene scene = new Scene(gridPane, 500, 500);

        
        primaryStage.setTitle("Fans Grid");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
