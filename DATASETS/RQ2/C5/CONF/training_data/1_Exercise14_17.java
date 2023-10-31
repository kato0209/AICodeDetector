

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.FileInputStream;
import java.io.IOException;


public class HangmanGame {

    private final static double HEIGHT = 320;
    private final static double WIDTH = 300;

    @Override
    public void start(Stage primaryStage) {
        FXMLLoader fxmlLoader = new FXMLLoader();
        try {
            Parent root = fxmlLoader.load(new FileInputStream("ch_14/exercise14_17/hangman.fxml"));
            primaryStage.setTitle(getClass().getName());
            root.setTranslateX(20); 
            Scene scene = new Scene(root, WIDTH, HEIGHT);
            primaryStage.setScene(scene);
            primaryStage.setResizable(false);
            primaryStage.show();

        } catch (IOException ioException) {
            ioException.printStackTrace();
        }
        

    }
}
