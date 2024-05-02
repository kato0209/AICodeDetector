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
   <extra_id_0>    private int hour;
   <extra_id_1> int minute;
    private int second;
    
    private double width = 400;
    <extra_id_2> height = 400;
    <extra_id_3>  <extra_id_4> DefaultClock() {
        LocalTime now = LocalTime.now();
       <extra_id_5> = now.getHour();
        this.minute = now.getMinute();
     <extra_id_6>  <extra_id_7> now.getSecond();
      <extra_id_8> 
       