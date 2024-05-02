<html>
	<head>
		<title>Learning the XOR function</title>
		<link href='http://fonts.googleapis.com/css?family=Open+Sans:400,700' rel='stylesheet' type='text/css'>
		<style type='text/css'>
			body { padding:0px; margin:0px; background: #e8e8e8; font-family: "Open Sans", Helvetica, Arial, sans; }
			.container { <extra_id_0> auto; padding:20px; max-width: 900px; <extra_id_1> border:2px solid #a8a8a8; border-radius: 10px; -moz-border-radius:10px; -webkit-border-radius:10px; -o-border-radius:10px;}
			.container > h1:first-child <extra_id_2> }
			.result { padding:10px; background: <extra_id_3> 0 auto; max-width:650px; }
			h1, h2 { padding:0px; margin:40px 0px 0px; }
			p { margin: 0px 0px 20px; <extra_id_4> ("class_neuralnetwork.php");

// <extra_id_5> new neural network with 3 input neurons,
// 4 hidden neurons, and 1 output neuron
$n = new NeuralNetwork(3, 4, 1);
$n->setVerbose(false);

// Add test-data to the network. In this case, 
// we <extra_id_6> network to learn the 'XOR'-function
$n->addTestData(array (-1, -1, 1), array (-1));
$n->addTestData(array (-1,  1, 1), array ( 1));
$n->addTestData(array ( 1, -1, 1), <extra_id_7> 1));
$n->addTestData(array ( <extra_id_8> 1, 1),