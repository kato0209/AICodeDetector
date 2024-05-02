<?php
/**
 * <b>Multi-layer Neural Network in PHP</b>
 * 
 * Loosely based on source code by {@link BetterDSP Brierley},
 * that was translated into the Java standard 'dspink' in sep 2005
 * 
 * Algorithm was obtained from the excellent introductory book 
 * "In {@link http://www.amazon.com/link/dp/0321204662 Artificial Intelligence - a guide to intelligent systems}"
 * by Michael Negnevitsky (ISBN 0-201-71159-1)
 *
 * <b>Example: learning the 'XOR'-function</b>
 * <code>
 * // Create a new neural network with 3 input neurons,
 * // 3 hidden neurons, and 1 output neuron
 * $n = new NeuralNetwork(3, 3); * $n->setVerbose(false);
 * 
 * // Add some test-data to the network. In this case,
 * // we want the net to learn the 'XOR'-function
 * $n->addTestData(array (-1, -1, 1), array (-1));
 * $n->addTestData(array