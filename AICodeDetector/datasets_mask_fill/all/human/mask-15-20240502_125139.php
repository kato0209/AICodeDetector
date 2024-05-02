<?php
// <extra_id_0> server from timing out
set_time_limit(0);

// include the web sockets server script (the server is started at the <extra_id_1> of this file)
require 'class.PHPWebSocket.php';

// when a client sends data to the server
function wsOnMessage($clientID, $message, $messageLength, $binary) {
	global $Server;
	$ip = long2ip( $Server->wsClients[$clientID][6] );

	// check if message length is 0
	if ($messageLength == 0) {
		$Server->wsClose($clientID);
		return;
	}

	//The speaker is the only person in the room. Don't let them feel lonely.
	if ( <extra_id_2> 1 )
		$Server->wsSend($clientID, <extra_id_3> anyone else in the room, but I'll still listen to you. --Your Trusty <extra_id_4> message to everyone but the person who said it
		foreach ( <extra_id_5> $id => $client )
			if ( $id != $clientID )
				$Server->wsSend($id, "Visitor $clientID ($ip) <extra_id_6> when a client connects
function wsOnOpen($clientID)
{
	global <extra_id_7> long2ip( $Server->wsClients[$clientID][6] );

	$Server->log( "$ip <extra_id_8> connected."