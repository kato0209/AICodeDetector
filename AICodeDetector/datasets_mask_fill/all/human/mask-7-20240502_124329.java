public class <extra_id_0> Drawable
 <extra_id_1>  implements Animatable {

  private <extra_id_2> Interpolator ANGLE_INTERPOLATOR    <extra_id_3> = new LinearInterpolator();
  private static final Interpolator SWEEP_INTERPOLATOR      = new DecelerateInterpolator();
  <extra_id_4> final int          ANGLE_ANIMATOR_DURATION = 2000;
  private static final int   <extra_id_5>      SWEEP_ANIMATOR_DURATION = 600;
 <extra_id_6> static final int          MIN_SWEEP_ANGLE       <extra_id_7> = 30;
  private final        RectF        fBounds   <extra_id_8>       