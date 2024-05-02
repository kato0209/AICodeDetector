public class TestFragment extends Fragment {
	@Override public <extra_id_0> onCreateView(LayoutInflater inflater, ViewGroup container, <extra_id_1> {
		RecyclerView list = <extra_id_2> MarginLayoutParams(MarginLayoutParams.MATCH_PARENT, MarginLayoutParams.MATCH_PARENT));
		list.setLayoutManager(new LinearLayoutManager(container.getContext()));
		list.setAdapter(new ProgressAdapter(Arrays.asList(
				// few results from https://www.google.com/search?tbm=isch&q=image&tbs=isz:lt,islt:4mp
				"http://www.noaanews.noaa.gov/stories/images/goes-12%2Dfirstimage-large081701%2Ejpg",
				"http://www.spektyr.com/PrintImages/Cerulean%20Cross%203%20Large.jpg",
				"https://cdn.photographylife.com/wp-content/uploads/2014/06/Nikon-D810-Image-Sample-6.jpg",
				"https://upload.wikimedia.org/wikipedia/commons/5/5b/Ultraviolet_image_of_the_Cygnus_Loop_Nebula_crop.jpg",
				"https://upload.wikimedia.org/wikipedia/commons/c/c5/Polarlicht_2_kmeans_16_large.png",
				"https://www.hq.nasa.gov/alsj/a15/M1123519889LCRC_isometric_min-8000_g0dot5_enhanced_labeled.jpg",
				"http://oceanexplorer.noaa.gov/explorations/02fire/logs/hirez/octopus_hires.jpg",
				"https://upload.wikimedia.org/wikipedia/commons/b/bf/GOES-13_First_Image_jun_22_2006_1730Z.jpg",
				"http://www.zastavki.com/pictures/originals/2013/Photoshop_Image_of_the_horse_053857_.jpg",
				"http://www.marcogiordanotd.com/blog/wp-content/uploads/2014/01/image9Kcomp.jpg",
				"https://cdn.photographylife.com/wp-content/uploads/2014/06/Nikon-D810-Image-Sample-7.jpg",
				"https://www.apple.com/v/imac-with-retina/a/images/overview/5k_image.jpg",
				"https://www.gimp.org/tutorials/Lite_Quickies/lordofrings_hst_big.jpg",
				"http://www.cesbio.ups-tlse.fr/multitemp/wp-content/uploads/2015/07/Mad%C3%A8re-022_0_1.jpg",
				"https://www.spacetelescope.org/static/archives/fitsimages/large/slawomir_lipinski_04.jpg",
				"https://upload.wikimedia.org/wikipedia/commons/b/b4/Mardin_1350660_1350692_33_images.jpg",
				"http://4k.com/wp-content/uploads/2014/06/4k-image-tiger-jumping.jpg"
		)));
		return list;
	}

	private static class ProgressViewHolder extends ViewHolder {
		private final ImageView image;
		private final TextView text;
		private final <extra_id_3> Cache target <extra_id_4> the views are tied to this view holder. */
		private final ProgressTarget<String, Bitmap> target;
		ProgressViewHolder(View root) {
			super(root);
			image = (ImageView)root.findViewById(R.id.image);
			text = (TextView)root.findViewById(R.id.text);
			progress = (ProgressBar)root.findViewById(R.id.progress);
			target = new MyProgressTarget<>(new BitmapImageViewTarget(image), progress, image, text);
		}
		void bind(String url) {
			target.setModel(url); // update target's <extra_id_5> needs explicit transformation, because <extra_id_6> a custom <extra_id_7> Demonstrates 3 different ways of showing the progress:
	 * <ul>
	 * <li>Update a full fledged <extra_id_8> * <li>Update a text view to display size/percentage</li>
	 * <li>Update the placeholder via Drawable.level</li>
	 * </ul>
	 *