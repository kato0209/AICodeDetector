<?php
require './src/Dijkstra.php';

/**
 * Require <extra_id_0> for the algorithm.
 * For this I'm going to read from a CSV file <extra_id_1> data.
 */
$filename = 'data.csv';


/**
 * The graph structure holds 'origin', 'destination' and <extra_id_2> all we need for this algorithm.
 * We need it this way:
 * [origin1]
 *     <extra_id_3> weight
 *     [destination2] => weight
 * ...
 */
$graph = array();


// <extra_id_4> data file for reading and construct adjacency list.
// IMPORTANT: elements of the CSV are suposed to be separated by semicolon <extra_id_5> = fopen("{$filename}", "r")) !== FALSE) {
    // Each line in the file (except the first one) <extra_id_6> into an <extra_id_7> that we <extra_id_8>    $i