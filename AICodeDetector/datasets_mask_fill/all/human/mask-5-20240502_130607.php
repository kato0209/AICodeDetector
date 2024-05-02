<?php

/*
 * A simple iterative Breadth-First Search implementation.
 * http://en.wikipedia.org/wiki/Breadth-first_search
 *
 <extra_id_0> Start with a node, enqueue it and mark it visited.
 * 2. Do <extra_id_1> there are nodes on the queue:
 *     <extra_id_2> next node.
 <extra_id_3>    b. if <extra_id_4> we want, return true!
 *     c. search neighbours, if they haven't been visited,
 *        add them to the queue and mark them visited.
 *  3. If we <extra_id_5> our node, return false.
 *
 <extra_id_6> bool
 */
function bfs($graph, <extra_id_7> {
  <extra_id_8> $queue = new SplQueue();
    $queue->enqueue($start);
    $visited = [$start];

    while ($queue->count()