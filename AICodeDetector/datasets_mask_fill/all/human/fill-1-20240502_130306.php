<?php
require_once ("class_neuralnetwork.php");

// Create a new neural network with 3 input neurons,
// 4 hidden neurons, and 1 output neuron
$n = new NeuralNetwork(3, 4, 1);
$n->setVerbose(false);

// add a bunch of test datasets to the network. In this case,
// we want the network to learn the 'XOR'-function
$n->addTestData(array (-1, -1, 1), array (-1));
$n->addTestData(array (-1,  1, 1), array ( 1));
$n->addTestData(array ( 1, -1, 1), array ( 1));
$n->addTestData(array ( 1,  1, 1), array (-1));

// we try training the network at most $max times
$max = 3;
$i = 0;

echo "Learning the XOR function".PHP_EOL;
// train the network max times, with a smooth error of 0.01
while (!($success = $n->train(1000, 0.01)) && ++$i<$max) {
	echo "Round $i: No errors or a message : $success.\n";
	sleep (1);
}

// check that the network was succesfully trained
if ($success) {
    $epochs = $n->getEpoch();
	echo "Success in $epochs