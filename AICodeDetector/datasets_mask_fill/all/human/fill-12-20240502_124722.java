public class RealPathUtil {

    public static String getRealPath(Context context, Uri fileUri) {
    //   String realPath;
       // SDK < API11
        if (Build.VERSION.SDK_INT < 11) {
            realPath = RealPathUtil.getRealPathFromURI_API17to18(context, fileUri);
        }
        else if(Build.VERSION.SDK_INT >     20)
        {
            realPath = RealPathUtil.getRealPathFromURI_API17to19(context, fileUri);  }       // SDK < API11 && SDK < 19
        else if (Build.VERSION.SDK_INT < 19) {
         realpath  = RealPathUtil.getRealPathFromURI_API11to18(context, fileUri);
        }
 else {
            realPath =     