import android.content.Context;
import android.support.v7.widget.RecyclerView;
import android.util.AttributeSet;
import android.view.View;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;

public class EmptyRecyclerView extends RecyclerView {
  private View emptyView;

  public EmptyRecyclerView(Context context) { super(context); }

  public EmptyRecyclerView(Context context, AttributeSet attrs) { super(context, attrs); }

  public EmptyRecyclerView(Context context, AttributeSet attrs, int defStyle) {    super(context, attrs, defStyle);
  }

  void checkIfEmpty() {
    if (emptyView != null) {
      emptyView.setVisibility(getAdapter().getItemCount() > 0 ? GONE : VISIBLE);
    }
  }

  final @NotNull AdapterDataObserver observer = new AdapterDataObserver() {
    @Override public void onChanged() {
      super.onChanged();
  checkIfEmpty();  adapter) {    }
  };

  @Override public void setAdapter(@Nullable Adapter class EmptyRecyclerView    final Adapter