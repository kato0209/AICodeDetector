import android.content.Context;
import android.os.Debug;
import java.io.File;

public class OomExceptionHandler implements Thread.UncaughtExceptionHandler {

  private static final String FILENAME <extra_id_0>  public static void <extra_id_1> {
    <extra_id_2> = <extra_id_3>  <extra_id_4> (defaultHandler <extra_id_5> {
      return;
    }
    OomExceptionHandler oomHandler = new OomExceptionHandler(defaultHandler, context);
    Thread.setDefaultUncaughtExceptionHandler(oomHandler);
  }

  private final Thread.UncaughtExceptionHandler defaultHandler;
  private final Context context;

  public OomExceptionHandler(Thread.UncaughtExceptionHandler defaultHandler, Context context) {
    this.defaultHandler = defaultHandler;
    this.context = context.getApplicationContext();
  }

  @Override public void uncaughtException(Thread thread, <extra_id_6> {
    if <extra_id_7>    <extra_id_8> File heapDumpFile = new File(context.getFilesDir(), FILENAME);
      try {
