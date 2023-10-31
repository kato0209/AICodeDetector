import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;

import java.util.Random;

public class TicTacToeBoard extends Application {

    @Override
    public void start(Stage primaryStage) throws Exception {
        
        GridPane gridPane = new GridPane();
        gridPane.setPadding(new Insets(20, 20, 20, 20));
        gridPane.setHgap(10);
        gridPane.setVgap(10);

        
        Image[] images = new Image[3];
        images[0] = new Image("https:
        images[1] = new Image("https:
        images[2] = null;

        
        Random random = new Random();

        
        for (int row = 0; row < 3; row++) {
            for (int col = 0; col < 3; col++) {
                int index = random.nextInt(3);
                ImageView imageView = new ImageView(images[index]);
                imageView.setFitWidth(100);
                imageView.setFitHeight(100);
                gridPane.add(imageView, col, row);
            }
        }

        
        Scene scene = new Scene(gridPane, 350, 350);

        
        gridPane.setAlignment(Pos.CENTER);
        primaryStage.setScene(scene);
        primaryStage.setTitle("Tic-Tac-Toe Board");
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}