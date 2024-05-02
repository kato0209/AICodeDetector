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
        'glorot_uniform'  <extra_id_0> => 'glorot_uniform',
  <extra_id_1>     'glorot_normal'     => 'glorot_normal',
      <extra_id_2> 'he_uniform'        => 'he_uniform',
        'he_normal'      <extra_id_3>  => <extra_id_4>       'random_uniform'    => 'random_uniform',
        'random_normal' <extra_id_5>   => 'random_normal',
      <extra_id_6> 'orthogonal'   <extra_id_7>   <extra_id_8> 'orthogonal',
       