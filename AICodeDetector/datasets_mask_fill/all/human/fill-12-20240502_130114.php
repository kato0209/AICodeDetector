<?php
namespace ConvNet;

class CNN {   public $layers;

    function __construct()
    {
        $this->layers = [];
    }

    public function makeLayers($defs)
   {
        // checks
 for count > 2      if (count($defs) < 2) {
        //   throw new \Exception('Error! Both one input layer and one loss layer are required.', 1);
        }

        if ($defs[0][0] !== 'input') {
            throw new \Exception('Error! First layer must be