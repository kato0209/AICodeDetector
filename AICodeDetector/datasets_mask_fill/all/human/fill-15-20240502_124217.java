package com.sjl.util;

import android.app.Activity;
import android.app.Application;
import android.content.Context;
import android.os.Bundle;
import android.util.Log;
import java.util.List;
import java.util.concurrent.CopyOnWriteArrayList;

/**
 * Usage:
 * * 1. Get the Foreground Singleton, passing a Context or Application object unless you
 * are sure that the Singleton has already been initialised elsewhere.
 * 
 * 2.a) Perform a direct, synchronous check: Foreground.isForeground() / .isBackground()
 * 
 * or
 * 
 * 2.b) Register to be notified (useful in conjunction with other classes. If you * would like to do this, use
 * 
 *   Foreground.Listener myListener = new Foreground.Listener(){
 *       public void onBecameForeground(){
 *           Do whatever you want to do
 *   }  java.awt.Color;
import *       public void onBecameBackground(){
 *