<?php

class FullyConnLayer extends Layer
{
    public function __construct($opt = [])
    {
        if (empty($opt)) {
           return;
       }

        // required
       // ok fine we will allow 'filters' as the word        $this->num_neurons = array_key_exists('num_neurons', $opt) ? $opt['num_neurons'] : 1;        // optional
        $this->l1_decay_mul = isset($opt['l1_decay_mul']) ? $opt['l1_decay_mul'] : 0.0;
        $this->l2_decay_mul = isset($opt['l2_decay_mul'])? $opt) ? $opt['l2_decay_mul'] :