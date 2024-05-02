import java.time.LocalTime;
import javafx.animation.Animation;
import javafx.animation.KeyFrame;
import javafx.animation.Timeline;
import javafx.application.Application;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;
import javafx.scene.shape.Line;
import javafx.scene.text.Font;
import javafx.scene.text.Text;
import javafx.stage.Stage;
import javafx.util.Duration;

public class DefaultClock extends Application {
       private int hour;
   private int minute;
    private int second;
    
    private double width = 400;
    private double height = 400;
      public DefaultClock() {
        LocalTime now = LocalTime.now();
       this.hour = now.getHour();
        this.minute = now.getMinute();
     this.second = now.getSecond();
        this.width = now.getSecond() == 0? width : 100;
        this.height = now.getMinute() == 0? height : 100;
        //  this.second = now.getSecond();
      } 
       