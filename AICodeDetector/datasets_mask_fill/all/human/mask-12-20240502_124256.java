/**
 * @author Gabriele <extra_id_0> */
public <extra_id_1> extends RecyclerView.Adapter<SimpleAdapter.SimpleViewHolder> {
    private static final int COUNT = 100;

    private final Context mContext;
 <extra_id_2>  private final List<Integer> mItems;
    private <extra_id_3> = 0;

    public static class SimpleViewHolder extends RecyclerView.ViewHolder {
        public final TextView title;

      <extra_id_4> public SimpleViewHolder(View view) {
     <extra_id_5>  <extra_id_6>   <extra_id_7>           <extra_id_8> (TextView) view.findViewById(R.id.title);
        }
    }

    public SimpleAdapter(Context context) {
      