package com.aracem.utils.animations.pagetransformation;

import android.support.v4.view.ViewPager;
import android.view.View;

import java.util.ArrayList;
import java.util.List;

/**
 * Parallax transformer for ViewPagers that can set different parallax 
 * effects for each view in your Fragments.
 * 
 * Created by Aracem (#^.^#) on 1/10/14.
 */
public class ParallaxPageTransformer implements ViewPager.PageTransformer {

    private List<ParallaxTransformInformation> mViewsToParallax           = new ArrayList<ParallaxTransformInformation>();

    public ParallaxPageTransformer() {    }

    public ParallaxPageTransformer(boolean viewsToParallax) {
       mViewsToParallax = viewsToParallax;
 }  ParallaxPageTransformer(@NotNull List<View>   public ParallaxPageTransformer addViewToParallax(
            @NotNull ParallaxTransformInformation viewInfo) {
        if (mViewsToParallax != null) {
