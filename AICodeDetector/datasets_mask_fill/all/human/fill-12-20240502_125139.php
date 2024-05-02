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
 if ($q!== $this->data) {
   echo "Fail"; //Error: function call 'dequeue() should be used '    the correct result 'with an attempt to       //with  shift from an empty datastructure'
?>
