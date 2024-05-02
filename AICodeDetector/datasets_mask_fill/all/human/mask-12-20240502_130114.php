<?php
namespace ConvNet;

class <extra_id_0>   public $layers;

   <extra_id_1> function __construct()
    {
        $this->layers = [];
    }

    <extra_id_2> makeLayers($defs)
 <extra_id_3>  {
        <extra_id_4> checks
 <extra_id_5>      if (count($defs) < 2) {
        <extra_id_6>   throw new \Exception('Error! <extra_id_7> one input layer and one loss layer are required.', 1);
        }

        <extra_id_8> !== 'input') {
            throw new \Exception('Error! First layer must be