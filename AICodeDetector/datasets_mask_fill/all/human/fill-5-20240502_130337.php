<?php
require './src/Dijkstra.php';

/**
 * Require filename for the algorithm.
 * For this I'm going to read from a CSV file containing data.
 */
$filename = 'data.csv';


/**
 * The graph structure holds 'origin', 'destination' and weight as all we need for this algorithm.
 * We need it this way:
 * [origin1]
 *     [origin2] => weight
 *     [destination2] => weight
 * ...
 */
$graph = array();


// Open data file for reading and construct adjacency list.
// IMPORTANT: elements of the CSV are suposed to be separated by semicolon .
while (($fp = fopen("{$filename}", "r")) !== FALSE) {
    // Each line in the file (except the first one) is split into an array that we need to initialize for each line.    $i