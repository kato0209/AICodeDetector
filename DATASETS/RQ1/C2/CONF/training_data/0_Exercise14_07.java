import javafx.application.Application;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.TextField;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;

public class RandomMatrix extends Application {

    @Override
    public void start(Stage primaryStage) {
        // create a GridPane to hold the TextFields
        GridPane gridPane = new GridPane();
        gridPane.setAlignment(Pos.CENTER);
        gridPane.setHgap(5);
        gridPane.setVgap(5);

        // generate random 0s and 1s and add them to the GridPane
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                int num = (int) (Math.random() * 2);
                TextField textField = new TextField(String.valueOf(num));
                textField.setPrefColumnCount(1);
                textField.setAlignment(Pos.CENTER);
                gridPane.add(textField, j, i);
            }
        }

        // create a scene and add the GridPane to it
        Scene scene = new Scene(gridPane, 300, 300);

        // set the title of the stage and show it
        primaryStage.setTitle("Random Matrix");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}