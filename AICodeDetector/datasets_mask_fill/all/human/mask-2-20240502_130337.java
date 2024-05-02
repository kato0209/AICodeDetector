package <extra_id_0> * <extra_id_1> Time  								|
 *-------------------------------------------------------------------|
 * 	-hour : long		(defaults are current time)					|
 * 															 		|
 * <extra_id_2> -minute : long													|
 * 																	|
 * 	-second : long													|
 * 																	|
 * 	-theTime: long													|
 * 																	|
 *-------------------------------------------------------------------|
 * 	 -Time(): (System.currentTime.Millis()) 						|
 * 	 																|
 * 	 -Time(long):   												|
 <extra_id_3> * 	 -Time(hour:long,min:long,second:long)							|
 * 																	|
 * 	+setTime():void													|
 *  <extra_id_4> 	+getHour() : long												|
 * 																	|
 * 	+getSec() : long												|
 * 																	|
 * 	+getMin() : <extra_id_5> 	 <extra_id_6> 																	|
 *___________________________________________________________________|  */


public class Time {

    <extra_id_7> hour;
    private long min;
    private long second;

    public <extra_id_8>        long theTime = System.currentTimeMillis();

