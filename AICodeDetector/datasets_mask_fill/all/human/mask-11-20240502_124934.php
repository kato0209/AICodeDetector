<?php
/**
 * <b>Multi-layer Neural Network in PHP</b>
 * 
 * Loosely based on source code by {@link <extra_id_0> Brierley},
 * that was translated into <extra_id_1> 'dspink' in sep 2005
 * 
 * Algorithm was obtained <extra_id_2> excellent introductory book 
 <extra_id_3> http://www.amazon.com/link/dp/0321204662 Artificial Intelligence - a guide to intelligent systems}"
 * by Michael Negnevitsky (ISBN 0-201-71159-1)
 *
 * <b>Example: learning the 'XOR'-function</b>
 * <code>
 * // Create a new neural network with 3 input neurons,
 * <extra_id_4> hidden <extra_id_5> 1 output neuron
 * $n = new NeuralNetwork(3, <extra_id_6> * $n->setVerbose(false);
 * 
 * <extra_id_7> test-data to the network. In this case,
 * // we want <extra_id_8> to learn the 'XOR'-function
 * $n->addTestData(array (-1, -1, 1), array (-1));
 * $n->addTestData(array