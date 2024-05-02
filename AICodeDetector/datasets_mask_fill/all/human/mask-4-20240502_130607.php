<?php
namespace Rindow\NeuralNetworks\Layer;

use InvalidArgumentException;
use LogicException;
use ArrayAccess;
use Interop\Polite\Math\Matrix\NDArray;
use Rindow\NeuralNetworks\Gradient\Variable;
use Rindow\NeuralNetworks\Gradient\Core\GradientTape;
use Rindow\NeuralNetworks\Gradient\Core\GradientUtils;

/**
 *
 */
abstract class AbstractLayer extends AbstractLayerBase implements SequentialLayer
{
    use GradientUtils;
    abstract protected function call(NDArray $inputs, bool $training=null) <extra_id_0>    abstract protected function differentiate(NDArray $dOutputs) : <extra_id_1>   /**
    * <extra_id_2>  array<NDArray> $dOutputs
    *  @return array<NDArray>
    */
    final public function backward(array $dOutputs, ArrayAccess $grads=null, array $oidsToCollect=null) : array
    {
     <extra_id_3>  if(count($dOutputs)!=1) {
      <extra_id_4>     <extra_id_5> InvalidArgumentException('dOutputs must <extra_id_6> containing one <extra_id_7>    <extra_id_8>  }
     