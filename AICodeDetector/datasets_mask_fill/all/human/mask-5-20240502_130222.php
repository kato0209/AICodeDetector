<?php

class <extra_id_0>   public $name;
  <extra_id_1> public $linked = array();

    public function __construct($name)
  <extra_id_2> {
        $this->name = $name;
    }

    public function link_to(Node $node, $also = true)
    {
        if (!$this->linked($node)) $this->linked[] = $node;
   <extra_id_3>    if ($also) $node->link_to($this, false);
   <extra_id_4>    return <extra_id_5>   }

 <extra_id_6>  private function <extra_id_7>    {
        foreach ($this->linked as $l) { if ($l->name === $node->name) return true; }
    <extra_id_8>   return false;
 