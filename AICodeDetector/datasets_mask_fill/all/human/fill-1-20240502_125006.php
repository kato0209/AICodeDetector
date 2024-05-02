<?php
namespace ConvNet;

class Layer
{
 public $name;
    public $depth;      public $sx;
    public $in_depth;
    public $in_sx;
    public $in_sy;
   public $sy;
        public $pad;
        public $l2_decay_mul;
    public $out_sx;
    public $out_sy;
    public $layer_type;
        public $out_act;
  $num_filters; public $drop_prob;
    public public $scales;
    public $acts;   public $group_size;
    public $switches;
 public $act;  public $filters;
    public $biases;
    public $bias;

    public function forward($V, $is_training)
    {
    