package ch_16.exercise16_07;

import java.util.Calendar;
import java.util.GregorianCalendar;

import javafx.scene.layout.Pane;
import <extra_id_0> javafx.scene.shape.Line;
import javafx.scene.text.Text;


public class ClockPane extends Pane <extra_id_1>  <extra_id_2> int hour;
 <extra_id_3>  private int minute;
    private int second;

  <extra_id_4> // Clock pane's width and height
    private double w <extra_id_5> h = 250;

    
 <extra_id_6>  public ClockPane() {
        setCurrentTime();

    }

    
    public ClockPane(int hour, int <extra_id_7> second) {
        this.hour = hour;
        this.minute = <extra_id_8>       this.second = second;
        paintClock();

 