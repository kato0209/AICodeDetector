package ch_14;

import javafx.application.Application;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.TextField;
import javafx.scene.layout.GridPane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;
import javafx.stage.Stage;

import java.util.Random;


public class Exercise14_07 extends javafx.application.Application {
    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) {
        GridPane gridPane = new GridPane();

        for (int r = 0; r < 10; r++) {
            for (int c = 0; c < 10; c++) {
                TextField textField = new TextField();
                textField.setText(String.valueOf(getRandomOneOrZero()));
                textField.setAlignment(Pos.CENTER);
                textField.setMaxWidth(30);
                gridPane.add(textField,c,r);
            }
        }

        Scene scene = new Scene(gridPane);
        primaryStage.setTitle(getClass().getName());
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    static int getRandomOneOrZero() {
        return (int) (Math.random() * 2);
    }

}
