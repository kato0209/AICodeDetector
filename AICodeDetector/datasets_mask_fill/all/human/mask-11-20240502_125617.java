import android.content.Context;
import android.support.v7.widget.RecyclerView;
import android.util.AttributeSet;
import android.view.View;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;

public <extra_id_0> extends RecyclerView {
  <extra_id_1> emptyView;

  public EmptyRecyclerView(Context context) { super(context); }

  <extra_id_2> context, <extra_id_3> { super(context, attrs); }

  <extra_id_4> context, AttributeSet attrs, int <extra_id_5>    super(context, attrs, defStyle);
  }

  void checkIfEmpty() {
    if (emptyView != null) {
      emptyView.setVisibility(getAdapter().getItemCount() > 0 ? GONE : VISIBLE);
    }
  }

  final @NotNull AdapterDataObserver observer = new AdapterDataObserver() {
    @Override public void onChanged() {
      super.onChanged();
  <extra_id_6>  <extra_id_7>    }
  };

  @Override public void setAdapter(@Nullable Adapter <extra_id_8>    final Adapter