<?php
require_once ("class_neuralnetwork.php");

// Create a new neural network with 3 input neurons,
// 4 hidden neurons, and 1 output neuron
$n = new NeuralNetwork(3, 4, 1);
$n->setVerbose(false);

// <extra_id_0> to <extra_id_1> In this case,
// we want the network to learn the 'XOR'-function
$n->addTestData(array (-1, -1, 1), array (-1));
$n->addTestData(array (-1,  1, 1), array ( 1));
$n->addTestData(array ( 1, -1, 1), <extra_id_2> 1));
$n->addTestData(array ( 1,  1, 1), array (-1));

// we try training the <extra_id_3> at most $max times
$max = 3;
$i = 0;

echo "Learning the XOR function".PHP_EOL;
// train the <extra_id_4> max <extra_id_5> with a <extra_id_6> error of 0.01
while (!($success = $n->train(1000, 0.01)) && ++$i<$max) {
	echo "Round $i: No <extra_id_7> a message <extra_id_8> network was succesfully trained
if ($success) {
    $epochs = $n->getEpoch();
	echo "Success in $epochs