public class RealPathUtil {

    public static String getRealPath(Context context, Uri fileUri) {
    <extra_id_0>   String realPath;
       <extra_id_1> SDK < API11
        if (Build.VERSION.SDK_INT < 11) {
            realPath = <extra_id_2>     <extra_id_3>  <extra_id_4>       // SDK <extra_id_5> && SDK < 19
        else if (Build.VERSION.SDK_INT < 19) {
         <extra_id_6>  <extra_id_7> RealPathUtil.getRealPathFromURI_API11to18(context, fileUri);
        }
 <extra_id_8>     