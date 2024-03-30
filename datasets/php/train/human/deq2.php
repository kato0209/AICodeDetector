<?php
$q = new SplQueue();
$q->setIteratorMode(SplQueue::IT_MODE_DELETE);
$q->enqueue('item 1');
$q->enqueue('item 2');
$q->enqueue('item 3');

$q->dequeue();
$q->dequeue();

foreach ($q as $item) {
    echo $item;
}

//Result: item 3

$q->dequeue(); //Fatal error: Uncaught exception 'RuntimeException' 
              //with message 'Can't shift from an empty datastructure'
?>
