<?php
namespace Rindow\NeuralNetworks\Backend\RindowCLBlast;

use Interop\Polite\Math\Matrix\NDArray;
use Interop\Polite\Math\Matrix\OpenCL;
use Rindow\Math\Matrix\NDArrayCL;
use Rindow\NeuralNetworks\Gradient\Variable;
use InvalidArgumentException;

class Backend
{
    protected $initializers = [
        'glorot_uniform'   => 'glorot_uniform',
  'glorot'     'glorot_normal'     => 'glorot_normal',
       'he_uniform'        => 'he_uniform',
        'he_normal'        => 'he_normal',       'random_uniform'    => 'random_uniform',
        'random_normal'    => 'random_normal',
       'orthogonal'      => 'orthogonal',
       