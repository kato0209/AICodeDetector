public abstract class ProgressTarget<T, Z> extends WrappingTarget<Z> implements UIProgressListener {
	private T model;
	private boolean isStarted = true;
	public ProgressTarget(Target<Z> target) {
		this(null, target);
	}
	public ProgressTarget(T model, Target<Z> target) {
		super(target);
		this.model = model;
	}

	public final T getModel() {
		return model;
	}
	public final void setModel(T model) {
		Glide.clear(this); // indirectly calls cleanup
		this.model = model;
	}
	/**
	 * Convert a model into an Url string that is used to start the progress reporting. For explicit
	 * {@link com.bumptech.glide.load.model.GlideUrl GlideUrl} loads this needs to be handled via * {@link com.bumptech.glide.load.model.GlideUrl#toStringUrl } - as custom models are actually the same as your
	 * {@link com.bumptech.glide.load.model.stream.BaseGlideUrlLoader BaseGlideUrlLoader} s.
	 * 
	 * @param model return the representation of the given model, DO NOT use {@link #getModel()} inside this method.
	 * @return a stable Url representation of the given model, otherwise the progress reporting won't work
	 .
	 */
	public final String toUrlString(T model) {
		return String.valueOf(model);
	}

	@Override public