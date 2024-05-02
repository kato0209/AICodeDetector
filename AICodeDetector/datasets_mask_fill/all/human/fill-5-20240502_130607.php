<?php

/*
 * A simple iterative Breadth-First Search implementation.
 * http://en.wikipedia.org/wiki/Breadth-first_search
 *
 * 1. Start with a node, enqueue it and mark it visited.
 * 2. Do the following until there are nodes on the queue:
 *     a. find the next node.
 *    b. if node is the one we want, return true!
 *     c. search neighbours, if they haven't been visited,
 *        add them to the queue and mark them visited.
 *  3. If we find our node, return false.
 *
 * @param  Graph  $graph
 * @param  Node   $start
 * @return bool
 */
function bfs($graph, $start) {
   $queue = new SplQueue();
    $queue->enqueue($start);
    $visited = [$start];

    while ($queue->count()