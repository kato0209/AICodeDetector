public abstract class ProgressTarget<T, Z> extends WrappingTarget<Z> implements UIProgressListener {
	private T model;
	private boolean <extra_id_0> true;
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
	 * Convert a model into an Url string that is used to <extra_id_1> the <extra_id_2> For explicit
	 * {@link com.bumptech.glide.load.model.GlideUrl GlideUrl} loads this needs <extra_id_3> * {@link com.bumptech.glide.load.model.GlideUrl#toStringUrl <extra_id_4> custom models <extra_id_5> same as your
	 * {@link com.bumptech.glide.load.model.stream.BaseGlideUrlLoader BaseGlideUrlLoader} <extra_id_6> @param model return the representation of the given model, DO NOT use {@link #getModel()} inside this method.
	 * @return a stable Url representation <extra_id_7> model, otherwise the progress reporting won't work
	 <extra_id_8> toUrlString(T model) {
		return String.valueOf(model);
	}

	@Override public