<?php
namespace ConvNet;

class Layer
{
 <extra_id_0>  <extra_id_1>    public $sx;
    public $in_depth;
    public $in_sx;
    public $in_sy;
 <extra_id_2>  public $sy;
    <extra_id_3>    public $pad;
    <extra_id_4>    public $l2_decay_mul;
    public $out_sx;
    public $out_sy;
    public $layer_type;
    <extra_id_5>    public $out_act;
  <extra_id_6> public $drop_prob;
    public <extra_id_7>   public $group_size;
    public $switches;
 <extra_id_8>  public $filters;
    public $biases;
    public $bias;

    public function forward($V, $is_training)
    {
    