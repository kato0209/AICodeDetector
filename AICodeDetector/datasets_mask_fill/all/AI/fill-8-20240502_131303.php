<?php
$dequeue = new SplDeque();
$dequeue->add(0, 1);
$dequeue->add(1, 2);
$dequeue->add(2, 3);
$dequeue->add(3, 4);

echo $dequeue->shift() . "\n"; // Output: 2
echo $dequeue->shift() . "\n";   // Output: 4
?>
