<?php
// <body text='black'> となります
$bodytag = str_replace("%body%", "black", "<body text='%body%'>");

// Hll Wrld f PHP となります
$vowels = array("a", "e", "i", "o", "u", "A", "E", "I", "O", "U");
$hellotext = str_replace($vowels, "", "Hello World of PHP");

// You should eat pizza, beer, and ice cream every day となります
$phrase = "You should eat fruits, vegetables, and fiber every day.";
$healthy = array("fruits", "vegetables", "fiber");
$yummy  = array("pizza", "beer", "ice ");

$phrase = str_replace($healthy, $yummy, $phrase);

// good golly miss molly!
$counter = str_replace("ll", "", "good golly miss molly!", $count);
echo $count;
?>
