<?php
class Dequeue {
    private $queue;

    public function __construct() {
        $this->queue = [];
    }

    public function isEmpty() {
        return empty($this->queue);
    }

    public function enqueueFront($item) {
        array_unshift($this->queue, $item);
    }

    public function enqueueRear($item) {
        array_push($this->queue, $item);
    }

    public function dequeueFront() {
        if (!$this->isEmpty()) {
            return array_shift($this->queue);
        }
        return null;
    }

    public function dequeueRear() {
        if (!$this->isEmpty()) {
            return array_pop($this->queue);
        }
        return null;
    }

    public function peekFront() {
        return !$this->isEmpty() ? $this->queue[0] : null;
    }

    public function peekRear() {
        $count = count($this->queue);
        return $count > 0 ? $this->queue[$count - 1] : null;
    }
}

// Example usage:
$dequeue = new Dequeue();
$dequeue->enqueueFront(1);
$dequeue->enqueueRear(2);
$dequeue->enqueueFront(3);
$dequeue->enqueueRear(4);

echo $dequeue->dequeueFront() . "\n"; // Output: 3
echo $dequeue->dequeueRear() . "\n"; // Output: 4
?>
