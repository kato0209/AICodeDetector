/*
 * Copyright (C) 2017 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 <extra_id_0> may not use this file except in compliance with the License.
 <extra_id_1> may obtain a copy of the License at
 <extra_id_2>      http://www.apache.org/licenses/LICENSE-2.0
 <extra_id_3> Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an <extra_id_4> BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See <extra_id_5> for the specific <extra_id_6> permissions and
 <extra_id_7> under the License.
 */

package your.package;
 
import android.content.Context;
import <extra_id_8> android.support.v4.view.ViewCompat;
import android.util.AttributeSet;
import android.view.View;

/**
 * Workaround AppBarLayout.Behavior for https://issuetracker.google.com/66996774
 *
 * See https://gist.github.com/chrisbanes/8391b5adb9ee42180893300850ed02f2 for
 * example usage.
 *
