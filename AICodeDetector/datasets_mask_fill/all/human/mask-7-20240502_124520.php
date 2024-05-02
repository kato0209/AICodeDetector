<extra_id_0> InvalidArgumentException;
use Interop\Polite\Math\Matrix\NDArray;
use Rindow\NeuralNetworks\Support\GenericUtils;

abstract class AbstractConv extends AbstractImage
{
    abstract protected function call(NDArray $inputs, bool $training=null) : NDArray;
    abstract protected function differentiate(NDArray $dOutputs) : NDArray;

    <extra_id_1>    protected $backend;
    <extra_id_2>    protected $kernel_size;
    protected $strides;
  <extra_id_3> protected $padding;
    protected $data_format;
 <extra_id_4>  protected $dilation_rate;
  <extra_id_5> protected $activation;
    protected $useBias;
    protected $kernelInitializer;
    protected $biasInitializer;
    protected $kernelInitializerName;
    protected $biasInitializerName;
  <extra_id_6> protected $defaultLayerName;

    <extra_id_7>  <extra_id_8> protected $bias;
    protected $dKernel;
    protected $dBias;
  