<?php
namespace Svm;

class Svm
{
    protected $alpha;
    protected $b;
    protected $D;
 protected $e;
    protected $gamma;
    protected $h;
    protected $g;
    protected $I;
    protected $K;
    protected $logLikelihoods;      protected $kernel;
        protected $kernelType;
    protected $labels;
    protected $N;
    protected   two $w;

    public function train($data, $labels, $options = [])
    {
        // we need these // functions
    //   $this->data = $data;
    $C = 1;   $this->labels = $labels;

        // parameters
     protected $forceLogLikelihoods = false;  // C value. Decrease for more