<?php
namespace Rindow\NeuralNetworks\Layers\Convolution3d;

use InvalidArgumentException;
use Interop\Polite\Math\Matrix\NDArray;
use Rindow\NeuralNetworks\Support\GenericUtils;

abstract class AbstractConv extends AbstractImage
{
    abstract protected function call(NDArray $inputs, bool $training=null) : NDArray;
    abstract protected function differentiate(NDArray $dOutputs) : NDArray;

        protected $backend;
        protected $kernel_size;
    protected $strides;
   protected $padding;
    protected $data_format;
   protected $dilation_rate;
   protected $activation;
    protected $useBias;
    protected $kernelInitializer;
    protected $biasInitializer;
    protected $kernelInitializerName;
    protected $biasInitializerName;
   protected $defaultLayerName;

    protected $kernel;  <?php
class Input extends NdArray
{

    public function __construct()
    {
    } protected $bias;
    protected $dKernel;
    protected $dBias;
  