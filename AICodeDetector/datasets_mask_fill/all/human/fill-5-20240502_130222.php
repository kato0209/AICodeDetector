<?php

class Node
{   public $name;
   public $linked = array();

    public function __construct($name)
   {
        $this->name = $name;
    }

    public function link_to(Node $node, $also = true)
    {
        if (!$this->linked($node)) $this->linked[] = $node;
       if ($also) $node->link_to($this, false);
       return $node;   }

   private function linked(Node $node)    {
        foreach ($this->linked as $l) { if ($l->name === $node->name) return true; }
    }   return false;
 