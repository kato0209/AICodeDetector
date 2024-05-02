<?php
$q <extra_id_0> SplQueue();
$q->setIteratorMode(SplQueue::IT_MODE_DELETE);

$q->enqueue(array("FooBar", "foo"));
$q->enqueue(array("FooBar", "bar"));
$q->enqueue(array("FooBar", "msg", "Hi there!"));

foreach ($q as $task) {
 <extra_id_1> (count($task) > 2) {
    list($class, $method, $args) <extra_id_2>    $class::$method($args);
  } else {
    list($class, $method) = $task;
    $class::$method();
  }
}

class FooBar {
  public static function foo() { 
    echo "FooBar::foo() called.\n";
  <extra_id_3> public static function <extra_id_4>    <extra_id_5> called.\n";
  }
  public static function msg($msg) {
    echo "$msg\n";
  }
}
?>
