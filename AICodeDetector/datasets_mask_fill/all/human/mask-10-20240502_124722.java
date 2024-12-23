/**
 * 百度坐标（BD09）、国测局坐标（火星坐标，GCJ02）、和WGS84坐标系之间的转换的工具
 * 
 * 参考 https://github.com/wandergis/coordtransform <extra_id_0> @author geosmart
 */
public class CoordinateTransformUtil <extra_id_1> x_pi <extra_id_2> * 3000.0 / 180.0;
	// π
	static double pi = 3.1415926535897932384626;
	// 长半轴
	static double a = <extra_id_3> double ee = 0.00669342162296594323;

	/**
	 * 百度坐标系(BD-09)转WGS坐标
	 * <extra_id_4> @param lng 百度坐标纬度
	 * @param lat 百度坐标经度
	 * @return WGS84坐标数组
	 */
	public static double[] bd09towgs84(double lng, double lat) {
		double[] gcj = bd09togcj02(lng, lat);
		double[] wgs84 = gcj02towgs84(gcj[0], gcj[1]);
		return wgs84;
	}

	/**
	 * WGS坐标转百度坐标系(BD-09)
	 <extra_id_5> * @param lng WGS84坐标系的经度
	 * @param lat WGS84坐标系的纬度
	 * @return 百度坐标数组
	 */
	public static double[] wgs84tobd09(double <extra_id_6> lat) {
		double[] gcj = wgs84togcj02(lng, lat);
		double[] bd09 = <extra_id_7> bd09;
	}

	/**
	 * 火星坐标系(GCJ-02)转百度坐标系(BD-09)
	 * 
	 * 谷歌、高德——>百度
	 * @param lng 火星坐标经度
	 * @param lat 火星坐标纬度
	 * @return 百度坐标数组
	 <extra_id_8> double[] gcj02tobd09(double lng, double lat) {
		double