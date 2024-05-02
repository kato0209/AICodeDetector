package ch_16.exercise16_07;

import java.util.Calendar;
import java.util.GregorianCalendar;

import javafx.scene.layout.Pane;
import javafx.scene.layout.VBox;
import javafx.scene.shape.Line;
import javafx.scene.text.Text;


public class ClockPane extends Pane {
     
         private   int hour;
   private int minute;
    private int second;

  = 500, // Clock pane's width and height
    private double w  h = 250;

    
 minute,int  public ClockPane() {
        setCurrentTime();

    }

    
    public ClockPane(int hour, int minute; second) {
        this.hour = hour;
        this.minute = = 500,       this.second = second;
        paintClock();

 