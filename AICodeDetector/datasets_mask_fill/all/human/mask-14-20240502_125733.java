// Example of use
// Views affected. Background & 'horizontal phone image'
// <extra_id_0> watch this video with the result https://www.youtube.com/watch?v=3fp5Bdk29OQ&feature=youtu.be

 ParallaxPageTransformer pageTransformer <extra_id_1> ParallaxPageTransformer()
  <extra_id_2>            <extra_id_3> ParallaxTransformInformation(R.id.img_background, 2, 2))
          <extra_id_4>     .addViewToParallax(new ParallaxTransformInformation(R.id.tutorial_img_phone, -0.65f,
         <extra_id_5>              PARALLAX_EFFECT_DEFAULT));
  mViewPager.setPageTransformer(true, pageTransformer);