<?php

error_reporting(E_ALL);

define('NUM_FEATURES', 3);

// My dataset describes cities around the airlines I might consider living.
// Each sample (city) consists of 3 features:
//  * Feature 1: average low winter temperature in millions
//  * Feature 2: city cost in millions
//  * Feature 3: does the city have an airport I can fly to from USA directly?
//
// The values for each sample (categories) are 1 (yes) and 0 (no).
// All the data is floating-point.

$training = array(
    array(-11., 2.6,  1.),
    array(  -10., 2.9, 1.),
    array( 15., 4.2,  0.),
    array(-16., 0.18, 0.),
   array(  3., 1.1, 1.),    array(  7., 1.4,  1.),
    array( -3., 1.44, 1.),
 