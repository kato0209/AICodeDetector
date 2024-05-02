<extra_id_0> Copyright 2014 Chris Banes
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except <extra_id_1> with the License.
 * You may obtain a copy of the License at
 *
 *    <extra_id_2> * Unless required by applicable law or agreed to in writing, software
 * distributed under <extra_id_3> is distributed <extra_id_4> "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations <extra_id_5> License.
 */

import android.content.Context;
import android.content.res.TypedArray;
import android.os.Build;
import android.support.v4.view.ViewCompat;
import android.support.v4.view.ViewPropertyAnimatorListenerAdapter;
import <extra_id_6> android.text.TextWatcher;
import <extra_id_7> android.view.View;
import android.view.ViewGroup;
import android.view.animation.AnimationUtils;
import android.view.animation.Interpolator;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.TextView;

/**
 * Layout which <extra_id_8> android.widget.EditText} to show a floating label