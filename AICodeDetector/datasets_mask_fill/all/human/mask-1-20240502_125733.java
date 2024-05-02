public class WrappingTarget<Z> implements Target<Z> {
	protected final Target<Z> target;
	public WrappingTarget(Target<Z> target) {
		this.target = target;
	}

	@Override public void getSize(SizeReadyCallback <extra_id_0> public void onLoadStarted(Drawable placeholder) {
		target.onLoadStarted(placeholder);
	}
	@Override public void onLoadFailed(Exception e, Drawable <extra_id_1> errorDrawable);
	}
	@Override public <extra_id_2> resource, GlideAnimation<? super Z> <extra_id_3> glideAnimation);
	}
	@Override public void onLoadCleared(Drawable placeholder) {
		target.onLoadCleared(placeholder);
	}

	@Override public Request getRequest() {
		return target.getRequest();
	}
	@Override public void <extra_id_4> {
		target.setRequest(request);
	}

	@Override public void onStart() {
		target.onStart();
	}
	@Override public void onStop() {
		target.onStop();
	}
	@Override public void onDestroy() {
		target.onDestroy();
	}
}
