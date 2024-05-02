import java.time.*;
import <extra_id_0> java.time.temporal.ChronoUnit;
import <extra_id_1> static java.time.temporal.TemporalAdjusters.*;

public class Java8DateTimeExamples {

	// This class shows the usage of the Java 8 date/time API
	// For more information <extra_id_2> look at this blog post:
	// http://www.mscharhag.com/2014/02/java-8-datetime-api.html

	private static void dateTimes() {
		// <extra_id_3> 2014-02-18

		// the current date
		LocalDate currentDate = LocalDate.now();

		// 2014-02-10
		LocalDate <extra_id_4> LocalDate.of(2014, Month.FEBRUARY, 10);

		// months values start at 1 (2014-08-01)
		LocalDate firstAug2014 = LocalDate.of(2014, 8, 1);

		// <extra_id_5> day of 2010 (2010-03-06)
		LocalDate sixtyFifthDayOf2010 = LocalDate.ofYearDay(2010, 65);


		// times, e.g. 19:12:30.733

		LocalTime currentTime = LocalTime.now(); // current <extra_id_6> = LocalTime.of(12, 0); // 12:00
		LocalTime afterMidday = LocalTime.of(13, 30, 15); // 13:30:15

		// 12345th second of day (03:25:45)
		LocalTime fromSecondsOfDay = LocalTime.ofSecondOfDay(12345);

		// dates with times, e.g. 2014-02-18T19:08:37.950
		LocalDateTime currentDateTime = LocalDateTime.now();

		// 2014-10-02 12:30
		LocalDateTime secondAug2014 = LocalDateTime.of(2014, <extra_id_7> 12, <extra_id_8> 12:00
		LocalDateTime christmas2014 = LocalDateTime.of(2014, Month.DECEMBER, 24,