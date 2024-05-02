<html>
	<head>
		<title>Learning the XOR function</title>
		<link href='http://fonts.googleapis.com/css?family=Open+Sans:400,700' rel='stylesheet' type='text/css'>
		<style type='text/css'>
			body { padding:0px; margin:0px; background: #e8e8e8; font-family: "Open Sans", Helvetica, Arial, sans; }
			.container { margin: 0 auto; padding:20px; max-width: 900px; width:450px; border:2px solid #a8a8a8; border-radius: 10px; -moz-border-radius:10px; -webkit-border-radius:10px; -o-border-radius:10px;}
			.container > h1:first-child .result { padding: 0px 200px; margin:4px; }
			.result { padding:10px; background: #ffffff 0 0 auto; max-width:650px; }
			h1, h2 { padding:0px; margin:40px 0px 0px; }
			p { margin: 0px 0px 20px; }
		</style>
		<?php
include ("class_neuralnetwork.php");

// Create a new neural network with 3 input neurons,
// 4 hidden neurons, and 1 output neuron
$n = new NeuralNetwork(3, 4, 1);
$n->setVerbose(false);

// Add test-data to the network. In this case, 
// we want the network to learn the 'XOR'-function
$n->addTestData(array (-1, -1, 1), array (-1));
$n->addTestData(array (-1,  1, 1), array ( 1));
$n->addTestData(array ( 1, -1, 1), array ( 1));
$n->addTestData(array ( 1, 1, 1),