<?php
namespace ConvNet;

class ConvLayer extends Layer
{
  <extra_id_0> public function __construct($opt = [])
    {
        if (empty($opt)) {
    <extra_id_1>       return;
  <extra_id_2>     }

      <extra_id_3> // required
        $this->out_depth = $opt['filters'];
  <extra_id_4>     // filter <extra_id_5> be odd if possible, it's cleaner.
      <extra_id_6> $this->sx = $opt['sx'];
        $this->in_depth = $opt['in_depth'];
       <extra_id_7> = $opt['in_sx'];
    <extra_id_8>   $this->in_sy = $opt['in_sy'];

     