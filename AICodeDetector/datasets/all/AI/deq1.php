<?php
class ListNode {
    public $value;
    public $next;

    public function __construct($val) {
        $this->value = $val;
        $this->next = null;
    }
}

class Dequeue {
    private $front;
    private $rear;

    public function __construct() {
        $this->front = null;
        $this->rear = null;
    }

    public function isEmpty() {
        return $this->front === null;
    }

    public function enqueueFront($val) {
        $newNode = new ListNode($val);
        if ($this->isEmpty()) {
            $this->rear = $newNode;
        } else {
            $newNode->next = $this->front;
        }
        $this->front = $newNode;
    }

    public function enqueueRear($val) {
        $newNode = new ListNode($val);
        if ($this->isEmpty()) {
            $this->front = $newNode;
        } else {
            $this->rear->next = $newNode;
        }
        $this->rear = $newNode;
    }

    public function dequeueFront() {
        if ($this->isEmpty()) {
            return null;
        }
        $val = $this->front->value;
        $this->front = $this->front->next;
        if ($this->front === null) {
            $this->rear = null;
        }
        return $val;
    }

    public function dequeueRear() {
        if ($this->isEmpty()) {
            return null;
        }
        $val = $this->rear->value;
        if ($this->front === $this->rear) {
            $this->front = $this->rear = null;
        } else {
            $current = $this->front;
            while ($current->next !== $this->rear) {
                $current = $current->next;
            }
            $current->next = null;
            $this->rear = $current;
        }
        return $val;
    }

    public function peekFront() {
        return $this->isEmpty() ? null : $this->front->value;
    }

    public function peekRear() {
        return $this->isEmpty() ? null : $this->rear->value;
    }
}

// Example usage:
$dequeue = new Dequeue();
$dequeue->enqueueFront(1);
$dequeue->enqueueRear(2);
$dequeue->enqueueFront(3);
$dequeue->enqueueRear(4);

echo $dequeue->dequeueFront() . "\n"; // Output: 3
echo $dequeue->dequeueRear() . "\n";  // Output: 4
?>
