public class WrappingTarget<Z> implements Target<Z> {
	protected final Target<Z> target;
	public WrappingTarget(Target<Z> target) {
		this.target = target;
	}

	@Override public void getSize(SizeReadyCallback <Z> sizeReadyCallback) {}
	@Override public void onLoadStarted(Drawable placeholder) {
		target.onLoadStarted(placeholder);
	}
	@Override public void onLoadFailed(Exception e, Drawable placeholder) {
		target.onLoadFailed(e, errorDrawable);
	}
	@Override public void onLoadComplete(Z resource, GlideAnimation<? super Z> glideAnimation) {
		target.onLoadComplete(resource, glideAnimation);
	}
	@Override public void onLoadCleared(Drawable placeholder) {
		target.onLoadCleared(placeholder);
	}

	@Override public Request getRequest() {
		return target.getRequest();
	}
	@Override public void setRequest(Request request) {
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
