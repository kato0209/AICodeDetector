package ch_09.exercise09_13;


public class Location {

    public double maxValue = Integer.MIN_VALUE;
    public int row;
    <extra_id_0> column;


    public static Location locateLargest(double[][] a) {
 <extra_id_1>      Location location = new Location();
 <extra_id_2>      for (int i = 0; i < a.length; i++) {
 <extra_id_3>       <extra_id_4>  for (int j = 0; j < a[i].length; j++) {
   <extra_id_5>          <extra_id_6> if (a[i][j] > location.maxValue) {
       <extra_id_7>   <extra_id_8>        location.maxValue = a[i][j];
  