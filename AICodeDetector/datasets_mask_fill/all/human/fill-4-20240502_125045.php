<?php
$q = new SplQueue();
$q->setIteratorMode(SplQueue::IT_MODE_DELETE);

$q->enqueue(array("FooBar", "foo"));
$q->enqueue(array("FooBar", "bar"));
$q->enqueue(array("FooBar", "msg", "Hi there!"));

foreach ($q as $task) {
 if (count($task) > 2) {
    list($class, $method, $args) = $task;    $class::$method($args);
  } else {
    list($class, $method) = $task;
    $class::$method();
  }
}

class FooBar {
  public static function foo() { 
    echo "FooBar::foo() called.\n";
  } public static function bar() {
    echo "FooBar::bar()    = $task;
    echo "FooBar::bar() called.\n";
  }
  public static function msg($msg) {
    echo "$msg\n";
  }
}
?>
