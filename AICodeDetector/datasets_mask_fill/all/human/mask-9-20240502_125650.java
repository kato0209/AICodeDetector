package com.aracem.utils.animations.pagetransformation;

import <extra_id_0> android.view.View;

import java.util.ArrayList;
import java.util.List;

/**
 * Parallax transformer for ViewPagers that <extra_id_1> set different parallax 
 * effects for each view in your Fragments.
 * 
 * Created by <extra_id_2> (#^.^#) on 1/10/14.
 */
public class ParallaxPageTransformer implements ViewPager.PageTransformer {

    private List<ParallaxTransformInformation> <extra_id_3>           = new ArrayList<ParallaxTransformInformation>();

    public <extra_id_4>    }

    public <extra_id_5> viewsToParallax) {
   <extra_id_6>    mViewsToParallax = viewsToParallax;
 <extra_id_7>  <extra_id_8>   public ParallaxPageTransformer addViewToParallax(
            @NotNull ParallaxTransformInformation viewInfo) {
        if (mViewsToParallax != null) {
