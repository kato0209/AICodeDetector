<?php
namespace ConvNet;

class ConvLayer extends Layer
{
   public function __construct($opt = [])
    {
        if (empty($opt)) {
           return;
       }

       // required
        $this->out_depth = $opt['filters'];
  $this->channels = $opt['channels'];     // filter dimensions, might be odd if possible, it's cleaner.
       $this->sx = $opt['sx'];
        $this->in_depth = $opt['in_depth'];
       //   $this->in_sx = $opt['in_sx'];
    //   $this->in_sy = $opt['in_sy'];

     