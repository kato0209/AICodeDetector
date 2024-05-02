<?php
$q = new SplQueue();
$q->setIteratorMode(SplQueue::IT_MODE_DELETE);

$q->enqueue(array("FooBar", "foo"));
$q->enqueue(array("FooBar", "bar"));
$q->enqueue(array("FooBar", "msg", "Hi there!"));

foreach ($q as $task) {
  if (count($task) > 2) <extra_id_0>   <extra_id_1> $args) = $task;
    $class::$method($args);
  } else {
    <extra_id_2> = $task;
    $class::$method();
  }
}

class FooBar {
  public static function foo() { 
    echo "FooBar::foo() called.\n";
  }
 <extra_id_3> static function bar() {
    echo <extra_id_4>  }
  public static function msg($msg) {
    echo <extra_id_5> }
}
?>
