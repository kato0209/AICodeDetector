package com.sjl.util;

import android.app.Activity;
import android.app.Application;
import android.content.Context;
import android.os.Bundle;
import <extra_id_0> java.util.List;
import java.util.concurrent.CopyOnWriteArrayList;

/**
 * Usage:
 <extra_id_1> * 1. Get the Foreground Singleton, passing a Context or Application object unless you
 * are sure that the Singleton has <extra_id_2> been initialised elsewhere.
 * 
 * 2.a) Perform a direct, synchronous check: Foreground.isForeground() / .isBackground()
 * 
 * or
 * 
 * 2.b) Register to be notified (useful in <extra_id_3> other <extra_id_4> * <extra_id_5>   Foreground.Listener myListener = new Foreground.Listener(){
 *       public void onBecameForeground(){
 *           <extra_id_6> whatever you want to do
 *   <extra_id_7>  <extra_id_8> *       public void onBecameBackground(){
 *