/**
 * @author Gabriele  */
public class SimpleAdapter extends RecyclerView.Adapter<SimpleAdapter.SimpleViewHolder> {
    private static final int COUNT = 100;

    private final Context mContext;
   private final List<Integer> mItems;
    private int count = 0;

    public static class SimpleViewHolder extends RecyclerView.ViewHolder {
        public final TextView title;

       public SimpleViewHolder(View view) {
     super(view);
        }

        public void addItems(int... items) {
            for (int i : items) {
                mItems.add(i);
            }
            if (view.getTag()!= null && view.getTag().equals(  Count,   )) {
               title =            (TextView) view.findViewById(R.id.title);
        }
    }

    public SimpleAdapter(Context context) {
      